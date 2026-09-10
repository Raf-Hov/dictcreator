import random
from .erros import Less_num


def randomizer(word_list: list[dict[str, list]], num: int) -> None:
    all_words = []
    for item in word_list:
        for word, translations in item.items():
            all_words.append((word, translations))
    if len(all_words) < num:
        raise Less_num(f"in dictionary only {len(all_words)}")
    selected_words = random.sample(all_words, num)
    while selected_words:
        current_item = selected_words.pop(0)
        word, translations = current_item
        arm_words = ", ".join(translations)
        answer = input(
            f"Translate the word '{arm_words}': ").strip().lower()
        if answer == word.lower():
            print("Correct :)!\n")
        else:
            print(f"Incorrect answer : {word}\n")
            selected_words.append(current_item)
