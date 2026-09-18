import random
from collections import deque


def randomizer(word_dicts: dict[str, dict[str, list]], num: int, dict_name: str) -> None:
    if dict_name not in word_dicts:
        raise KeyError(
            f"Dictionary '{dict_name}' not found. Available options: {list(word_dicts.keys())}")
    all_words = list(word_dicts[dict_name].items())
    if len(all_words) < num:
        raise ValueError(
            f"In '{dict_name}' dictionary only {len(all_words)} words available.")
    selected_list = random.sample(all_words, num)
    selected_words = deque(selected_list)
    available_words = [w for w in all_words if w not in selected_list]
    print(f"--- Starting quiz using the '{dict_name}' dictionary ---")
    print("Type 'skip' instead of an answer to skip a word.")
    while selected_words:
        print(f"Words left : {len(selected_words)}")
        current_item = selected_words.popleft()
        word, translations = current_item
        arm_words = ", ".join(translations)
        answer = input(f"Translate the word \033[31m'{arm_words}':\033[0m ").strip().lower()
        if answer == "skip":
            print(f"Skipped word: {word}")
            if available_words:
                new_item = random.choice(available_words)
                available_words.remove(new_item)
                selected_words.append(new_item)
                print("Added a new random word to the queue!\n")
            else:
                print("No more new words in dictionary to replace it.\n")
            continue
        if answer == word.lower():
            print("\033[32mCorrect :)!\033[0m\n")
        else:
            print(f"Incorrect answer : \033[31m{word}\033[0m\n")
            selected_words.append(current_item)
