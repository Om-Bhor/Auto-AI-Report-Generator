#  Requirements
"""
cryptography==45.0.5
google-genai
requests
python-docx
markdown
reportlab
beautifulsoup4
python-dotenv
"""

#  ----- Readme----
"""
1. Due to limitation of time i have just implemented the process of creating a report and storing it in a docx file.
2. Instead of just a python function calling manually, I can use langgraph and langchain for the workflow
3. I focused on delivering a functional end-to-end MVP. 
4. The system successfully automates the complete pipeline from user input to AI-generated research report and exports it as a professionally formatted Word document.
5. I intentionally designed the code in a modular way so each component—search, context building, report generation, and document export—can later be replaced by specialized LangGraph agents.
6. My next step would be to migrate this workflow to a multi-agent architecture using LangGraph and LangChain, add Retrieval-Augmented Generation (RAG) with a vector database, incorporate web content extraction, and deploy it as a scalable web application.
7. Testing Process:-
    open terminal activate the venv downdload the requirements and run command python app.py.
    wait till u see the message as stored successfully.
    once done you can get your report in the reports folder whith your topic name.

Thank You.
"""

import os
from agent.search_agent import search_company
# from agent.scraper_agent import extract_links
from agent.context_builder import build_context
from agent.writer_agent import generate_report
from agent.docx_generator import save_docx
from pathlib import Path

os.makedirs("report",exist_ok=True)
topic = input("Enter a topic: ")
print("\nSearching...\n")
search = search_company(topic)

context = build_context(search)
print("Generating report...\n")
response = generate_report(topic, context)
# print(response)

# Path("reports").mkdir(exist_ok=True)
# print(f"\n Saving the report in reports")
# with open(f"reports/{topic}.md", "w", encoding="utf-8") as f:
#     f.write(response)

# print(f"\nReport saved to reports/{topic}.md")

docx_path = save_docx(topic, response)
print(f"DOCX saved at: {docx_path}")

# articles = []
# for link in links:
#     text = fetch_article(link["links"])
#     articles.append(text)

# for item in articles:
#     print(item)