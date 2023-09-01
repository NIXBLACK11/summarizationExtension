import requests

# Define the URL of your Django summarization endpoint
url = "http://127.0.0.1:8000/summarizer/summarize/"

# Example input text
input_text = """
Scientists have discovered a new species of butterfly in the rainforests of South America. The butterfly, named Morpho stellaris, has striking iridescent blue wings that shimmer in the sunlight. Researchers believe that its unique coloration is a result of complex structural properties of its wing scales rather than pigments.The discovery of Morpho stellaris is significant as it sheds light on the incredible diversity of life in the rainforests. The butterfly's habitat is under threat due to deforestation and climate change, emphasizing the need for conservation efforts. The research team used advanced imaging techniques to study the butterfly's wings and understand the mechanisms behind its vivid coloration. This could have applications in various fields, including materials science and optics. The findings of the study have been published in the journal Nature Biodiversity. The researchers hope that their work will inspire further exploration of the rainforest's biodiversity and the development of strategies to protect endangered species and their habitats.
"""

# Define the payload with the input text
payload = {
    "input_text": input_text
}

# Send the POST request
response = requests.post(url, data=payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the summarized text from the response JSON
    data = response.json()
    summarized_text = data.get("summarized_text", "Summarization failed.")
    print("Summarized Text:")
    print(summarized_text)
else:
    print(f"Request failed with status code {response.status_code}")
