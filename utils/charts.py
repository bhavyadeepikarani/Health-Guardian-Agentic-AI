import matplotlib.pyplot as plt


def plot_probability(probability):

    fig, ax = plt.subplots(figsize=(4, 4))

    ax.pie(
        [probability, 1 - probability],
        labels=["Risk", "Safe"],
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Diabetes Risk")

    return fig