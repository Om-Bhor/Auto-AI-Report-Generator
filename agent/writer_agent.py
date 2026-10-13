import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_report(topic, context):

    prompt = f"""
You are an expert Business Research Analyst.

Your task is to write a detailed professional research report.

Topic:
{topic}

Research Sources:
{context}

Write a report with the following sections.

# Executive Summary

# Table of Contents

# Introduction

# Company Overview

# Products and Services

# Business Model

# Industry Overview

# Market Position

# Competitor Analysis

# SWOT Analysis

# Recent Developments

# Future Opportunities

# Risks

# Conclusion

# References

Instructions:

- Use only the provided research sources.
- If information is unavailable, explicitly mention it.
- Write in a professional tone.
- Minimum 2500 words.
- Return Markdown only.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )

    return response.text