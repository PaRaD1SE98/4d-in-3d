import pandas as pd
import plotly
import plotly.express as px


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


if __name__ == '__main__':
    plot_3d_to_2d()
    plot_4d_to_3d()
