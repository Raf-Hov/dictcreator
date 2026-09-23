import random
from collections import deque


def randomizer(word_dicts: dict, num: int, dict_name: str, is_random: bool = True) -> None:
    if dict_name not in word_dicts:
        raise KeyError(f"Dictionary '{dict_name}' not found. Available options: {list(word_dicts.keys())}")
    all_words = list(word_dicts[dict_name].items())
    if len(all_words) < num:
        raise ValueError(f"In '{dict_name}' dictionary only {len(all_words)} words available.")
    if is_random:
        selected_list = random.sample(all_words, num)
        available_words = [w for w in all_words if w not in selected_list]
    else:
        selected_list = all_words[:num]
        available_words = all_words[num:]
    selected_words = deque(selected_list)
    print(f"--- Starting using the '{dict_name}' dictionary ---")
    while selected_words:
        current_item = selected_words.popleft()
        word, parts = current_item
        is_json_format = False
        main_translation = ""
        examples = []
        if isinstance(parts, list) and len(parts) > 0 and isinstance(parts[0], str):
            main_translation = parts[0]
            examples = parts[1:]
        if isinstance(parts, dict):
            is_json_format = True
            main_translation = parts.get('translation', '')
            examples_raw = parts.get('examples', [])
            for ex in examples_raw:
                if isinstance(ex, dict) and 'sentence_en' in ex:
                    examples.append(ex)
        if not main_translation and isinstance(parts, list):
            main_translation = parts[0] if parts else ""
        if not is_random:
            print(f"\n[Queue: {len(selected_words) + 1} | Left in dict: {len(available_words)}] Word: \033[32m{word}\033[0m")
            ans = input("Enter - show translation | 'skip' - move to end | 'next' - replace with new: ").strip().lower()
            if ans == "next":
                print(f"Translation: \033[31m{main_translation}\033[0m")
                if available_words:
                    new_item = available_words.pop(0)
                    selected_words.append(new_item)
                    print("Added a new word as replacement!\n")
                continue
            if ans == "skip":
                print(f"Translation: \033[31m{main_translation}\033[0m")
                print("Word moved to the end of the queue without deletion.")
                selected_words.append(current_item)
                continue
            print(f"Translation: \033[33m{main_translation}\033[0m")
            if examples:
                print("\nExamples/Sentences:")
                idx = 0
                while True:
                    part = examples[idx]
                    if isinstance(part, dict):
                        en = part.get("sentence_en", "")
                        am = part.get("translation_am", "")
                        print(f"\033[36mArmenian: {am}\033[0m")
                        ans_sentence = input("Translate to English (or 'next' to stop): ").strip().lower()
                        if ans_sentence == "next":
                            break
                        print(f"Correct English: \033[32m{en}\033[0m\n")
                    else:
                        print(f"\033[36m- {part}\033[0m")
                        ans_sentence = input("Enter - next sentence | 'next' - stop examples: ").strip().lower()
                        if ans_sentence == "next":
                            break
                    idx = (idx + 1) % len(examples)
            
            continue
        print(f"\nWords in queue: {len(selected_words) + 1} | Left in dict: {len(available_words)}")
        answer = input(f"Translate the word \033[31m'{word}'\033[0m: ").strip().lower()
        if answer == "next":
            print(f"Translation: \033[31m{main_translation}\033[0m")
            print("Skipped word.")
            if available_words:
                if is_random:
                    new_item = random.choice(available_words)
                    available_words.remove(new_item)
                else:
                    new_item = available_words.pop(0)
                selected_words.append(new_item)
                print("Added a new word as replacement!\n")
            else:
                print("No more new words in the dictionary to replace it.\n")
            continue
        elif answer == "skip":
            print(f"Translation: \033[31m{main_translation}\033[0m")
            print("Skipped without deletion (moved to the end).")
            selected_words.append(current_item)
            continue
        correct = False
        if answer:
            valid_answers = [x.strip().lower() for x in main_translation.replace(";", ",").split(",")]
            for valid in valid_answers:
                clean_valid = valid.replace("(", "").replace(")", "").strip()
                if answer == valid or answer == clean_valid:
                    correct = True
                    break
            if not correct:
                for valid in valid_answers:
                    clean_valid = valid.replace("(", "").replace(")", "").strip()
                    words_in_valid = clean_valid.split()
                    if answer in words_in_valid:
                        correct = True
                        break
        if correct:
            print("\033[32mCorrect :)!\033[0m")
            print(f"Full translation: \033[33m{main_translation}\033[0m")
        else:
            print(f"Translation: \033[31m{main_translation}\033[0m")
            print("Incorrect answer! Moved to the end of the queue.\n")
            selected_words.append(current_item)
        if examples:
            print("\nExamples/Sentences:")
            
            if is_random:
                random.shuffle(examples)
            idx = 0
            while True:
                part = examples[idx]
                if isinstance(part, dict):
                    en = part.get("sentence_en", "")
                    am = part.get("translation_am", "")
                    print(f"\033[36mArmenian: {am}\033[0m")
                    ans_sentence = input("Translate to English (or 'next' to stop): ").strip().lower()
                    if ans_sentence == "next":
                        break 
                    print(f"Correct English: \033[32m{en}\033[0m\n")
                else:
                    print(f"\033[36m- {part}\033[0m")
                    ans_sentence = input("Enter - next sentence | 'next' - next word: ").strip().lower()
                    if ans_sentence == "next":
                        break 
                idx = (idx + 1) % len(examples)
