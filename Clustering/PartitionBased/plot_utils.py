import numpy as np
import plotly
import plotly.graph_objs as go

# Configure Plotly to be rendered inline in the notebook.
plotly.offline.init_notebook_mode()

class plot_utils:
    def __init__(self, img_data, title, num_pixels=10000, colors=None, fsize=(13,4)):
        self.img_data = img_data
        self.title = title
        self.num_pixels = num_pixels
        self.colors = colors
        self.fsize = fsize

    def colorSpace(self):
        if self.colors is None:
            self.colors = self.img_data

        rand = np.random.RandomState(42)
        index = rand.permutation(self.img_data.shape[0])[:self.num_pixels]
        colors = self.colors[index]
        R, G, B = self.img_data[index].T
        

        # Configure the trace.
        trace = go.Scatter3d(
            x=R,  # <-- Put your data instead
            y=G,  # <-- Put your data instead
            z=B,  # <-- Put your data instead
            mode='markers',
            marker={
                'size': 2,
                'opacity': 0.8,
                'color': colors,
            }
        )
        # Configure the layout.
        layout = go.Layout(
                scene = dict(
                xaxis_title='RED',
                yaxis_title='GREEN',
                zaxis_title='BLUE'),
                width=600,
                height=350,
                margin=dict(r=0, b=0, l=0, t=0)
        )

        plot_figure = go.Figure(data=[trace], layout=layout)
        plotly.offline.iplot(plot_figure)
