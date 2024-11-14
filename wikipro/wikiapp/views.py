from django.shortcuts import render
import wikipediaapi
from wikipediaapi import Wikipedia

# Define user-agent for Wikipedia access
user_agent = "MyWikipediaApp/1.0 (Contact: your-email@example.com)"
wiki_wiki = Wikipedia(language='en', user_agent=user_agent)

def fetch_and_save_summary(topic):
    page = wiki_wiki.page(topic)
    if page.exists():
        return page.summary
    else:
        return None

def summary_view(request):
    if request.method == "POST":
        topics = request.POST.get("topics").split(",")
        summaries = {}

        for topic in topics:
            topic = topic.strip()
            if topic:  # Only process non-empty topics
                summary = fetch_and_save_summary(topic)
                if summary:
                    summaries[topic] = summary
                else:
                    summaries[topic] = "This page does not exist or could not be found."

        return render(request, "results.html", {"summaries": summaries})

    return render(request, "form.html")
