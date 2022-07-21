import pandas as pd
import plotly
import plotly.express as px
import numpy as np


def oscillate_range(stop):
    """
    Generate 0, -1, 1, -2, 2, -3, 3, ..., -stop/2, stop/2
    """
    a, counter = 0, 0
    while True:
        if counter > stop:
            return
        yield a
        if a == 0:
            a -= 1
        elif a < 0:
            a = -a
        else:
            a = -a
            a -= 1
        counter += 1


def plot_3d_to_2d():
    df = pd.DataFrame({'x': [],
                       'y': [],
                       'z': [],
                       'r': []})

    for r in range(21):
        for x in oscillate_range(40):
            for y in oscillate_range(40):
                if x ** 2 + y ** 2 > r ** 2:
                    continue
                for z in oscillate_range(40):
                    r_calculated_2 = x ** 2 + y ** 2 + z ** 2
                    if not r_calculated_2 <= r ** 2:
                        break
                    else:
                        data = {'x': x,
                                'y': y,
                                'z': z,
                                'r': r}
                        df = pd.concat([df, pd.DataFrame(data, index=[0])])

    fig = px.scatter(data_frame=df, x='x', y='y', color='z', color_continuous_scale=plotly.colors.sequential.Viridis)
    fig.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
    )
    fig.show()
    fig.write_html('./3dto2d.html')


def plot_4d_to_3d():
    df4d = pd.DataFrame({'x': [],
                         'y': [],
                         'z': [],
                         'w': [],
                         'r': []})
    for r in range(11):
        for x in oscillate_range(20):
            for y in oscillate_range(20):
                if x ** 2 + y ** 2 > r ** 2:
                    continue
                for z in oscillate_range(20):
                    if x ** 2 + y ** 2 + z ** 2 > r ** 2:
                        continue
                    for w in oscillate_range(20):
                        r_calculated_2 = x ** 2 + y ** 2 + z ** 2 + w ** 2
                        if not r_calculated_2 <= r ** 2:
                            break
                        else:
                            data = {'x': x,
                                    'y': y,
                                    'z': z,
                                    'w': w,
                                    'r': r}
                            df4d = pd.concat([df4d, pd.DataFrame(data, index=[0])])
    fig = px.scatter_3d(df4d, x='x', y='y', z='z', color='w', color_continuous_scale=plotly.colors.sequential.Viridis)
    fig.update_traces(marker=dict(size=2))
    fig.show()
    fig.write_html('./4dto3d.html')


def matrix_plot_3d_to_2d():
    X = np.arange(-20, 20)
    Y = np.arange(-20, 20)
    Z = np.arange(-20, 20)
    x, y, z = np.meshgrid(X, Y, Z)
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    r_idx = np.where(r <= 15)
    df = pd.DataFrame({'x': X[r_idx[0]],
                       'y': Y[r_idx[1]],
                       'z': Z[r_idx[2]]})
    fig = px.scatter(data_frame=df, x='x', y='y', color='z', color_continuous_scale=plotly.colors.sequential.Viridis)
    fig.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
    )
    fig.show()
    fig.write_html('./3dto2d_matrix.html', include_plotlyjs='cdn')


def matrix_plot_4d_to_3d():
    X = np.arange(-20, 20)
    Y = np.arange(-20, 20)
    Z = np.arange(-20, 20)
    W = np.arange(0, 40)
    x, y, z, w = np.meshgrid(X, Y, Z, W)
    r = np.sqrt((x - 0) ** 2 + (y - 0) ** 2 + (z - 0) ** 2 + (w - 20) ** 2)
    r_idx = np.where(r <= 15)
    df4d = pd.DataFrame({'x': X[r_idx[0]],
                         'y': Y[r_idx[1]],
                         'z': Z[r_idx[2]],
                         'w': W[r_idx[3]]})
    fig = px.scatter_3d(df4d, x='x', y='y', z='z', color='w', color_continuous_scale=plotly.colors.sequential.Viridis)
    fig.update_traces(marker=dict(size=2))
    fig.show()
    fig.write_html('./4dto3d_matrix.html', include_plotlyjs='cdn')


if __name__ == '__main__':
    # plot_3d_to_2d()
    # plot_4d_to_3d()
    matrix_plot_3d_to_2d()
    matrix_plot_4d_to_3d()
