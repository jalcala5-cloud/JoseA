# Name: Jose Alcala
# Date: 10:16:2025
# Class: CIS188 

# Description: Multi-clipboard utility for quick text snippets.
import pyperclip  # type: ignore

# Predefined text snippets
TEXTS = {
    "Agree": "Yes, I agree. That sounds fine.",
    "Busy": "Sorry, I’m tied up right now.",
    "Thanks": "Thanks very much!",
    "Hi": "Hello User, How are you?",
    "Goodbye": '"You are fire"',
}


def get_key_from_input() -> str:
    """Prompt the user to enter a key."""
    return input(f"Enter a key ({', '.join(TEXTS.keys())}): ").strip()


def get_message(key: str) -> str | None:
    """Look up the message by key."""
    return TEXTS.get(key)


def copy_to_clipboard(message: str) -> None:
    """Copy message text to clipboard."""
    pyperclip.copy(message)


def main() -> None:
    """Main program logic."""
    key = get_key_from_input()

    message = get_message(key)
    if not message:
        print(f"No message found for key: '{key}'")
        return

    copy_to_clipboard(message)
    print(f"Message for key '{key}' copied to clipboard!")
    print(f"Content: {message}")


if __name__ == "__main__":
    main()

