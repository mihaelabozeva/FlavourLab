from django import template

register = template.Library()


@register.filter
def intensity_label(value):
    labels = {
        1: "Very mild",
        2: "Mild",
        3: "Medium",
        4: "Strong",
        5: "Very strong",
    }
    return labels.get(value, "Unknown")
