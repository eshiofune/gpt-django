import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_KEY"])


def generate_image(text_prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=text_prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return image_url


# For testing purposes
if __name__ == "__main__":
    prompt = """Generate an image that visually illustrates the essence of the following story.

    Once upon a time, in the kingdom of Eldoria, nestled in the heart of a dormant volcano, lived a dragon named Brimstone. Unlike the dragons of lore, Brimstone was not a ferocious beast, but a gentle giant with iridescent scales of sapphire blue.

    The villagers of Eldoria lived in constant fear of dragons due to the tales passed on through generations. They would hide and tremble at the mere mention of one. Brimstone, aware of their fears, kept his distance, limiting himself to the confines of his volcanic abode, and watching the villagers from afar with longing.

    One year, Eldoria experienced a harsh winter. The crops failed, and the villagers were on the brink of starvation. Brimstone, from his high vantage point, could see their plight. His heart ached at the sight of their suffering. He resolved to help.

    Brimstone had a massive hoard of fruits and vegetables, grown deep within the volcano from seeds brought by birds and wind from distant lands. He decided to share his trove with the villagers. Under the cover of night, he flew over the village, dropping fruits and vegetables. The villagers awoke to find the mysterious bounty, their fear momentarily forgotten in their hunger.

    This act continued for days. The villagers were baffled by the consistent replenishment of food, but grateful nonetheless. They named their anonymous benefactor the "Blue Benefactor."

    One day, a curious child named Ada decided to uncover the identity of the Blue Benefactor. She stayed awake, hidden in the shadows of her house, watching. When she spotted the silhouette of Brimstone in the moonlight, her initial fear was replaced with awe. She observed the dragon's gentle manner and kindness, and she realized that the Blue Benefactor was none other than Brimstone.

    Excitedly, Ada shared the truth with the villagers the next morning. The adults were hesitant and skeptical at first, recalling the stories of dragon terror. However, their perception gradually changed as they realized the dragon had been their savior.

    The villagers decided to approach Brimstone, to thank him. With Ada leading the way, they climbed the dormant volcano. Brimstone, surprised by their visit, warmly welcomed them. The villagers expressed their gratitude, and Brimstone, in return, was overjoyed to finally interact with them without inducing fear.

    From that day onwards, Brimstone and the villagers of Eldoria lived in harmony. The tale of the 'Benevolent Dragon' replaced the old scary stories, and the dragon and villagers became the symbols of unity and coexistence.

    And so, in the heart of the dormant volcano, lived a dragon named Brimstone, the sapphire-scaled friend of Eldoria, a symbol of kindness, generosity, and a legend in his own right.
    """
    print(generate_image(prompt))
