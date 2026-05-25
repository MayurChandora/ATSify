import os
import json
from groq import Groq

def analyze_resume_with_llm(resume_text, job_description):
    """
    Sends the parsed resume and JD to Groq API using LLaMA 3
    and expects a strictly formatted JSON response.
    """
    api_key = os.environ.get("GROQ_API_KEY")
    model = os.environ.get("LLAMA_MODEL", "llama3-8b-8192")
    
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in environment variables.")

    client = Groq(api_key=api_key)

    system_prompt = """You are an expert ATS (Applicant Tracking System) and senior technical recruiter. 
Your task is to analyze a candidate's resume against a job description.
You MUST output ONLY a valid JSON object with exactly these keys:
- "match_score": an integer from 0 to 100 representing how well the resume matches the JD.
- "missing_keywords": a list of strings representing critical keywords/skills in the JD that are missing from the resume.
- "strengths": a list of strings highlighting what the candidate does well based on the JD.
- "suggestions": a single string paragraph providing actionable tips to improve the resume for this specific job.

Do not include any markdown formatting like ```json in the output. Just output the raw JSON object.
"""

    user_prompt = f"""
Job Description:
{job_description}

Resume Text:
{resume_text}
"""

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                }
            ],
            model=model,
            temperature=0.2, # Low temperature for more deterministic/consistent JSON output
            response_format={"type": "json_object"}
        )
        
        output_str = response.choices[0].message.content
        return json.loads(output_str)

    except Exception as e:
        print(f"Error calling Groq API: {e}")
        # Return a fallback JSON in case of failure
        return {
            "match_score": 0,
            "missing_keywords": ["Error connecting to AI"],
            "strengths": ["None"],
            "suggestions": f"An error occurred during analysis: {str(e)}"
        }
