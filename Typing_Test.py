import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a widely used high-level programming language.",
    "Typing fast requires a lot of practice and patience.",
    "Artificial Intelligence is shaping the future of the world.",
    "Learning to code can open up many opportunities.",
    "A journey of a thousand miles begins with a single step.",
    "In the middle of difficulty lies opportunity.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.",
    "The only limit to our realization of tomorrow is our doubts of today.",
]

print("🧠 Typing Speed Test")
print("----------------------")
input("Press Enter when you are ready to start...")

test_sentence = random.choice(sentences)
print("\nType this sentence:\n")

print(test_sentence)
print("\nStart typing below:\n")

start_time = time.time()
typed = input(">>> ")
end_time = time.time()

time_taken = end_time - start_time
word_count = len(typed.split())
speed_wpm = word_count / (time_taken / 60)

# Accuracy
correct_chars = 0
for i in range(min(len(typed), len(test_sentence))):
    if typed[i] == test_sentence[i]:
        correct_chars += 1
accuracy = (correct_chars / len(test_sentence)) * 100

print("\n🕒 Time Taken: {:.2f} seconds".format(time_taken))
print("📈 Your Speed: {:.2f} WPM".format(speed_wpm))
print("🎯 Accuracy: {:.2f}%".format(accuracy))
