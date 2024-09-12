def count_words(text):
   return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    count = {}
    for ch in text.lower():
        if not ch.isalpha():
           continue
        if ch not in count:
          count[ch] = 1
        else:
          count[ch] += 1
    return count

def main():
  file_path = ""
  with open("books/frankenstein.txt") as f:
    text = f.read()

  wc = count_words(text)
  cc = count_characters(text)

  print(f"--- Begin report of {file_path} ---")
  print(f"{wc} words found in the document\n")

  for ch, count in sorted(cc.items(), key=lambda i: i[1], reverse=True):
    print(f"The '{ch}' character was found {count} times")
  print("--- End report ---")

if __name__ == "__main__":
   main()