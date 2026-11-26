"""Deadpan Forecasts for Cities That Do Not Exist.

Writes a single one-line weather forecast for an invented city to
/output/entry.txt (or $ENTRY_OUTPUT when set).

The line: an overnight forecast for Dribbleford, a city that does not
exist, delivered in the plain, confident tone of a TV meteorologist:
a hard freeze, a river solid enough to skate on, and ducks who have
already filed complaints about it.
"""

import os

ENTRY = (
    "Overnight in Dribbleford, temperatures fall to minus two, "
    "the river freezes solid enough to skate on, and the ducks "
    "have already filed complaints."
)

MAX_CHARS = 160
MIN_CHARS = 1


def check_single_line(text):
    """The entry must be exactly one line: no newlines inside it."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def check_length(text):
    """The gate requires 1 to 160 characters, not only whitespace."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        raise ValueError(
            "entry must be %d to %d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    return True


def check_city_named(text):
    """The forecast must name the invented city it is about."""
    if "Dribbleford" not in text:
        raise ValueError("entry must name the invented city Dribbleford")
    return True


def check_forecast_words(text):
    """The line must read as a weather forecast, not a bare joke."""
    lowered = text.lower()
    for word in ("temperatures", "river", "freezes"):
        if word not in lowered:
            raise ValueError("entry is missing forecast detail: %s" % word)
    return True


def check_deadpan_twist(text):
    """The deadpan twist must be present: the ducks' complaint."""
    if "ducks have already filed complaints" not in text:
        raise ValueError("entry is missing its deadpan twist")
    return True


def check_no_extra_whitespace(text):
    """No leading or trailing whitespace and no doubled spaces."""
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "  " in text:
        raise ValueError("entry has doubled spaces")
    return True


def check_ends_with_period(text):
    """A broadcast line ends with a full stop, like a read-out sentence."""
    if not text.endswith("."):
        raise ValueError("entry must end with a full stop")
    return True


def check_word_count(text):
    """The line should be tight: a broadcast sentence, not a paragraph."""
    words = text.split()
    if len(words) < 10 or len(words) > 40:
        raise ValueError("entry word count out of range: %d" % len(words))
    return True


def validate(text):
    """Run every check on the entry text before it is written out."""
    check_single_line(text)
    check_length(text)
    check_city_named(text)
    check_forecast_words(text)
    check_deadpan_twist(text)
    check_no_extra_whitespace(text)
    check_ends_with_period(text)
    check_word_count(text)
    return True


def main():
    validate(ENTRY)
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print("wrote %d characters to %s" % (len(ENTRY), output_path))


if __name__ == "__main__":
    main()
