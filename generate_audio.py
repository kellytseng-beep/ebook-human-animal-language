"""Generate MP3 audio files for the ebook using gTTS (Google Translate TTS)."""
from pathlib import Path
from gtts import gTTS

OUT = Path(__file__).parent / "audio"
OUT.mkdir(exist_ok=True)

ARTICLE_PARAGRAPHS = [
    ("p1",
     "Human language is a unique system of communication that allows people to share complex ideas, "
     "emotions, and experiences. Unlike animals, humans can use language to talk about the past, present, "
     "and future. This ability is called displacement. For example, a person can describe what happened "
     "yesterday or plan for tomorrow. Animals, however, usually communicate about immediate needs, such "
     "as food or danger."),
    ("p2",
     "Another important feature of human language is creativity. Humans can produce an unlimited number "
     "of sentences using a limited set of words and rules. This means we can express new ideas that have "
     "never been said before. In contrast, animal communication systems are more fixed. For instance, "
     "bees perform a dance to show the location of food, but this system does not change much or allow "
     "new meanings."),
    ("p3",
     "Human language also has a complex structure. It includes grammar, which is a set of rules that "
     "organizes words into meaningful sentences. These rules help us understand each other clearly. "
     "Animal communication does not have the same level of structure. While some animals, like dolphins "
     "or birds, can produce different sounds, these sounds do not follow detailed grammatical rules "
     "like human language."),
    ("p4",
     "Finally, human language is learned socially and culturally. Children learn language by interacting "
     "with others in their community. Culture plays a big role in shaping how language is used. On the "
     "other hand, many animal communication systems are mostly instinctive. This means animals are born "
     "with the ability to communicate in certain ways, without needing to learn complex rules from others."),
]

VOCAB = [
    ("communication",
     "communication. communication. People use communication to share ideas. "
     "Good communication is important in teamwork."),
    ("displacement",
     "displacement. displacement. Displacement allows us to talk about the future. "
     "Animals usually lack displacement."),
    ("immediate",
     "immediate. immediate. He needs immediate help. Animals react to immediate danger."),
    ("creativity",
     "creativity. creativity. Creativity is important in art. Children show creativity when they play."),
    ("express",
     "express. express. She can express her feelings well. Language helps us express ideas."),
    ("fixed",
     "fixed. fixed. The schedule is fixed. Animal signals are often fixed."),
    ("structure",
     "structure. structure. This building has a strong structure. Language structure is important."),
    ("grammatical",
     "grammatical. grammatical. This sentence is not grammatical. Students learn grammatical rules."),
    ("interacting",
     "interacting. interacting. Children learn by interacting with others. "
     "Social media helps people interact."),
    ("instinctive",
     "instinctive. instinctive. Birds have instinctive behaviors. His reaction was instinctive."),
]

def synth(text: str, out_path: Path):
    gTTS(text=text, lang="en", tld="us", slow=False).save(str(out_path))
    print(f"  ok {out_path.name}")

def main():
    print("Generating article paragraphs...")
    for name, text in ARTICLE_PARAGRAPHS:
        synth(text, OUT / f"article_{name}.mp3")
    print("Generating vocabulary...")
    for word, text in VOCAB:
        synth(text, OUT / f"vocab_{word}.mp3")
    print("Done.")

if __name__ == "__main__":
    main()
