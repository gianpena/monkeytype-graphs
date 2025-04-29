import json,sys
from datetime import datetime
import plotly.graph_objects as go

FILENAME = sys.argv[1]


def main():
    with open(f"{FILENAME}.json", "r", encoding="utf-8") as file:
        entries = json.load(file)


    entries.sort(key=lambda k:k['timestamp'])
    wpm = []
    acc = []
    consistency = []
    timestamps = []
    hover_text = []
    for entry in entries:
        if 'wpm' not in entry: continue
        if 'acc' not in entry: continue
        if 'consistency' not in entry: continue
        if 'timestamp' not in entry: continue
        wpm.append(entry['wpm'])
        acc.append(entry['acc'])
        consistency.append(entry['consistency'])
        timestamps.append(entry['timestamp'])
        hover_text.append(f'Race from {entry['name']}<br>Completed on {datetime.fromtimestamp(timestamps[-1] / 1000).strftime('%b %d, %Y at %H:%M:%S')}<br>WPM: {wpm[-1]}<br>Accuracy: {acc[-1]}%<br>Consistency: {consistency[-1]}%')

    oldest = timestamps[0]
    time_diffs = [(ts - oldest) for ts in timestamps]

    max_diff = max(time_diffs)
    color_values = [diff / max_diff for diff in time_diffs]

    fig = go.Figure(data=[go.Scatter3d(
        x=wpm,
        y=acc,
        z=consistency,
        mode='markers',
        hovertext=hover_text,
        hoverinfo='text',
        marker=dict(
            size=1,
            color=color_values,
            colorscale=[[0, 'red'], [0.5, 'yellow'], [1, 'green']],
            colorbar=dict(title="Time"),
            opacity=0.8
        )
    )])

    fig.update_layout(
        template="plotly_dark",
        width=800,
        height=800,
        scene=dict(
            xaxis=dict(range=[0, 305], title='WPM'),
            yaxis=dict(range=[0, 100], title='Accuracy (%)'),
            zaxis=dict(range=[0, 100], title='Consistency (%)'),
            bgcolor='rgb(17,17,17)'
        )
    )

    fig.write_html(f'{FILENAME}.html')


if __name__ == "__main__":
    main()