"""
AI Service for content generation using Google Gemini
Handles LLM calls for content generation, refinement, and template suggestions
"""

import os
import google.generativeai as genai
import json

# Try to load from .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed, use environment variables only

# Initialize Gemini client
api_key = os.getenv('GEMINI_API_KEY', 'AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk')
if not api_key:
    print("⚠️  WARNING: GEMINI_API_KEY not set. AI features will not work.")
    print("   Set it using: $env:GEMINI_API_KEY='your-key-here' (PowerShell)")
    print("   Or create a .env file with: GEMINI_API_KEY=your-key-here")

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize the model - using gemini-1.5-flash (faster and cost-effective)
# The model will be initialized per-request to handle different model availability
def get_model(prefer_quality=True):
    """
    Get an available Gemini model
    Args:
        prefer_quality: If True, prioritize pro models for better quality. If False, prioritize speed.
    """
    if not api_key:
        print("❌ ERROR: GEMINI_API_KEY is not set!")
        return None
    
    # Try models in order of preference
    # Note: Model names should NOT include "models/" prefix
    if prefer_quality:
        # Prioritize quality (pro models first)
        models_to_try = [
            'gemini-1.5-pro',             # High quality - best for reports
            'gemini-2.5-pro',             # Latest pro - excellent quality
            'gemini-pro-latest',           # Latest pro (alias)
            'gemini-2.0-flash',           # Fast and efficient
            'gemini-1.5-flash',           # Most commonly available
            'gemini-2.5-flash',           # Latest flash model
            'gemini-flash-latest',         # Latest flash (alias)
            'gemini-2.0-flash-001',       # Stable version
        ]
    else:
        # Prioritize speed (flash models first)
        models_to_try = [
            'gemini-1.5-flash',           # Most commonly available
            'gemini-2.0-flash',           # Fast and efficient
            'gemini-2.5-flash',           # Latest flash model
            'gemini-flash-latest',         # Latest flash (alias)
            'gemini-1.5-pro',             # High quality
            'gemini-2.5-pro',             # Better quality
            'gemini-pro-latest',           # Latest pro (alias)
            'gemini-2.0-flash-001',       # Stable version
        ]
    
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            # Test the model with a simple call
            try:
                test_response = model.generate_content("Say 'OK' if you can read this.")
                if test_response and test_response.text:
                    print(f"✅ Using model: {model_name}")
                    return model
            except Exception as test_e:
                print(f"⚠️  Model {model_name} failed test: {test_e}")
                continue
        except Exception as e:
            print(f"⚠️  Could not initialize model {model_name}: {e}")
            continue
    
    # If none work, try to get any available model from the list
    try:
        print("🔍 Searching for available models...")
        available_models = list(genai.list_models())
        print(f"Found {len(available_models)} available models")
        for m in available_models:
            if 'generateContent' in m.supported_generation_methods:
                # Extract model name (remove "models/" prefix if present)
                model_name = m.name.replace('models/', '') if m.name.startswith('models/') else m.name
                # Try flash or pro models first
                if 'flash' in model_name.lower() or 'pro' in model_name.lower():
                    try:
                        model = genai.GenerativeModel(model_name)
                        # Test the model
                        test_response = model.generate_content("Say 'OK'")
                        if test_response and test_response.text:
                            print(f"✅ Using available model: {model_name}")
                            return model
                    except Exception as test_e:
                        print(f"⚠️  Model {model_name} failed: {test_e}")
                        continue
    except Exception as e:
        print(f"❌ Error listing models: {e}")
    
    print("❌ ERROR: No working Gemini model found!")
    return None


def generate_content_section(project_topic, section_title, project_type, previous_sections=None):
    """
    Generate high-quality content for a specific section/slide using Gemini
    Context-aware generation based on project topic and previous sections
    Enhanced with professional writing standards and quality requirements
    """
    print(f"\n🔵 Starting content generation...")
    print(f"   Topic: {project_topic}")
    print(f"   Section: {section_title}")
    print(f"   Type: {project_type}")
    
    # Try to use a higher quality model first (pro models)
    # Use quality-focused model for better report generation
    model = get_model(prefer_quality=True)
    if not model:
        error_msg = "Gemini API key not configured or no working model found. Please check GEMINI_API_KEY environment variable."
        print(f"❌ {error_msg}")
        raise Exception(error_msg)
    
    try:
        # Build comprehensive context from previous sections (increased from 200 to 500 chars)
        context = ""
        if previous_sections:
            context = "\n\nPrevious sections in this document (for context and continuity):\n"
            for i, sec in enumerate(previous_sections, 1):
                content_preview = sec.get('content', '')[:500] if len(sec.get('content', '')) > 500 else sec.get('content', '')
                context += f"{i}. {sec.get('title', 'Untitled')}: {content_preview}\n"
            context += "\nEnsure your content flows naturally from these previous sections and maintains consistency in tone and style.\n"
        
        # Create enhanced prompt based on project type
        if project_type == 'powerpoint':
            prompt = f"""You are a professional presentation content writer. Generate high-quality, engaging content for a PowerPoint slide.

SLIDE TITLE: "{section_title}"
PRESENTATION TOPIC: {project_topic}
{context}

QUALITY REQUIREMENTS:
1. **Structure & Clarity**:
   - Use clear, concise language suitable for presentation
   - Organize content with bullet points or numbered lists when appropriate
   - Each point should be self-contained and easy to understand at a glance
   - Use parallel structure in lists

2. **Content Depth**:
   - Provide substantive, informative content (not just surface-level)
   - Include specific details, examples, or data points where relevant
   - Make it engaging and memorable for the audience
   - Balance brevity with meaningful information

3. **Professional Tone**:
   - Maintain a professional yet accessible tone
   - Use active voice where possible
   - Avoid jargon unless necessary, and explain technical terms
   - Ensure content is appropriate for a business or academic presentation

4. **Length & Format**:
   - Target: 3-6 key points or 2-4 short, well-structured paragraphs
   - Each point/paragraph should be substantial (not just one sentence)
   - Content should be comprehensive enough to stand alone but concise enough for a slide

5. **Coherence**:
   - If this is not the first slide, ensure smooth transition from previous content
   - Maintain consistency with the overall presentation topic
   - Build upon previous sections logically

Generate the slide content now. Return ONLY the content, without meta-commentary or explanations:"""
        else:  # word document
            prompt = f"""You are a professional technical writer and content expert. Generate comprehensive, high-quality content for a document section.

SECTION TITLE: "{section_title}"
DOCUMENT TOPIC: {project_topic}
{context}

QUALITY REQUIREMENTS:

1. **Structure & Organization**:
   - Begin with a clear topic sentence that introduces the section's main idea
   - Use well-structured paragraphs (4-6 sentences each) with clear topic sentences
   - Include smooth transitions between paragraphs
   - End with a concluding sentence that ties the section together
   - Use subheadings or formatting cues if the content naturally divides into subsections

2. **Content Depth & Quality**:
   - Write comprehensive, detailed content (target: 600-1200 words)
   - Include specific examples, case studies, or real-world applications
   - Provide data, statistics, or evidence where relevant and appropriate
   - Explain concepts thoroughly - assume the reader wants to understand deeply
   - Cover the topic from multiple angles when appropriate
   - Include practical insights, implications, or applications

3. **Professional Writing Standards**:
   - Use formal, professional language appropriate for academic or business documents
   - Maintain consistent tone throughout (professional, informative, authoritative)
   - Use active voice primarily, passive voice only when appropriate
   - Vary sentence structure for readability
   - Ensure proper grammar, spelling, and punctuation
   - Use precise, specific vocabulary (avoid vague terms)

4. **Coherence & Flow**:
   - If this is not the first section, provide a smooth transition from previous sections
   - Reference or build upon concepts from earlier sections when relevant
   - Maintain logical flow within the section
   - Ensure the content directly addresses the section title
   - Connect ideas clearly and logically

5. **Engagement & Clarity**:
   - Make the content engaging and interesting to read
   - Use concrete examples and analogies to illustrate abstract concepts
   - Break down complex ideas into understandable components
   - Use formatting (bullets, lists) when it improves clarity
   - Ensure the content is accessible to the target audience

6. **Completeness**:
   - Thoroughly explore the section topic
   - Address potential questions a reader might have
   - Provide sufficient detail to be valuable and informative
   - Include relevant context and background information

Generate the section content now. Return ONLY the well-written content, without meta-commentary, explanations, or markdown formatting (unless it's part of the content structure):"""
        
        # Call Gemini API with generation config for better quality
        print(f"📡 Calling Gemini API with enhanced quality settings...")
        
        # Configure generation parameters for better quality
        generation_config = {
            "temperature": 0.7,  # Balance creativity and consistency
            "top_p": 0.95,      # Nucleus sampling for better quality
            "top_k": 40,        # Limit vocabulary for coherence
            "max_output_tokens": 2048 if project_type == 'word' else 1024,
        }
        
        response = model.generate_content(
            prompt,
            generation_config=generation_config
        )
        
        if not response or not response.text:
            error_msg = "Gemini API returned empty response"
            print(f"❌ {error_msg}")
            raise Exception(error_msg)
        
        generated_content = response.text.strip()
        
        # Post-process to ensure quality
        # Remove any markdown headers that might have been added
        if generated_content.startswith('#'):
            lines = generated_content.split('\n')
            # Skip markdown headers at the start
            while lines and lines[0].strip().startswith('#'):
                lines.pop(0)
            generated_content = '\n'.join(lines).strip()
        
        # Validate minimum length
        min_length = 200 if project_type == 'word' else 100
        if len(generated_content) < min_length:
            print(f"⚠️  Warning: Generated content is shorter than expected ({len(generated_content)} chars)")
            # Could regenerate with a request for more detail, but for now just log
        
        print(f"✅ Generated {len(generated_content)} characters")
        print(f"   Preview: {generated_content[:150]}...")
        
        return generated_content
    
    except Exception as e:
        error_msg = f"Error generating content: {str(e)}"
        print(f"❌ {error_msg}")
        import traceback
        traceback.print_exc()
        raise Exception(error_msg)


def refine_content_section(original_content, refinement_prompt, section_title, project_topic):
    """
    Refine existing content based on user's refinement prompt
    Context-aware refinement that only affects the single targeted section
    
    Args:
        original_content: The current content of the section
        refinement_prompt: User's refinement request (e.g., "shorten to 100 words", "make more formal")
        section_title: Title of the section being refined
        project_topic: Main topic of the project (for context)
    
    Returns:
        str: Refined content
    
    Logs:
        - Prompt sent to LLM
        - Response received from LLM
    """
    print(f"\n🔵 Starting content refinement...")
    print(f"   Section: {section_title}")
    print(f"   Project Topic: {project_topic}")
    print(f"   Refinement Prompt: {refinement_prompt}")
    print(f"   Original Content Length: {len(original_content)} characters")
    
    model = get_model()
    if not model:
        error_msg = "Gemini API key not configured. Please set GEMINI_API_KEY environment variable."
        print(f"❌ {error_msg}")
        raise Exception(error_msg)
    
    try:
        # Build context-aware prompt - only includes this section's content
        prompt = f"""You are refining content for a single section of a document. Only modify the content provided below based on the user's refinement request.

Section Title: {section_title}
Project Context: {project_topic}

Original Content (ONLY THIS SECTION - do not modify other sections):
{original_content}

User's Refinement Request: {refinement_prompt}

Instructions:
- Apply the refinement request ONLY to the content above
- Maintain relevance to the project topic: {project_topic}
- Keep the content focused on the section title: {section_title}
- Return ONLY the refined content, without explanations or meta-commentary
- Do not add content about other sections
- Preserve the core meaning and information

Refined Content:"""

        # Log the prompt for auditability
        print(f"📝 LLM Prompt (first 200 chars): {prompt[:200]}...")
        
        # Call Gemini API
        print(f"📡 Calling Gemini API for refinement...")
        response = model.generate_content(prompt)
        
        if not response or not response.text:
            error_msg = "Gemini API returned empty response for refinement"
            print(f"❌ {error_msg}")
            raise Exception(error_msg)
        
        refined_content = response.text.strip()
        
        # Log the response for auditability
        print(f"✅ Refinement complete")
        print(f"   Refined Content Length: {len(refined_content)} characters")
        print(f"   Preview: {refined_content[:150]}...")
        
        return refined_content
    
    except Exception as e:
        error_msg = f"Error refining content: {str(e)}"
        print(f"❌ {error_msg}")
        import traceback
        traceback.print_exc()
        raise Exception(error_msg)


def generate_outline(main_topic, project_type, num_sections=5):
    """
    Generate document outline (sections for Word, slides for PowerPoint)
    """
    model = get_model()
    if not model:
        raise Exception("Gemini API key not configured. Please set GEMINI_API_KEY environment variable.")
    
    try:
        if project_type == 'powerpoint':
            prompt = f"""Generate a PowerPoint presentation outline for the topic: "{main_topic}"

Requirements:
- Create {num_sections} slide titles
- Each title should be clear and engaging
- Slides should flow logically
- Include an introduction and conclusion slide
- Return only the slide titles, one per line

Generate the slide titles:"""
        else:  # word document
            prompt = f"""Generate a document outline for the topic: "{main_topic}"

Requirements:
- Create {num_sections} section headers
- Each header should be descriptive and professional
- Sections should flow logically
- Include an introduction and conclusion section
- Return only the section headers, one per line

Generate the section headers:"""
        
        response = model.generate_content(prompt)
        outline_text = response.text.strip()
        
        # Parse the outline into a list
        outline_items = [line.strip() for line in outline_text.split('\n') if line.strip() and not line.strip().startswith('#')]
        
        # Clean up numbering if present
        cleaned_items = []
        for item in outline_items:
            # Remove leading numbers, dashes, bullets
            cleaned = item.lstrip('0123456789.-) ').strip()
            if cleaned:
                cleaned_items.append(cleaned)
        
        return cleaned_items[:num_sections]  # Return up to requested number
    
    except Exception as e:
        raise Exception(f"Error generating outline: {str(e)}")
