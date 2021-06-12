"""
Everything plotly-related
"""

import plotly.io as pio
import plotly.graph_objects as go
import yaml
import logging


def set_layout_template(colorscale, template_name="sai"):
    """Applies colorscale to graph

    Args:
            colorscale (list): list of colors in hex code
            template_name (str): name of the template to re-use

    Returns:
            None

    Example:

    """

    pio.templates[template_name] = go.layout.Template(
        layout_colorway=colorscale,
        layout_hovermode="closest",
        layout_font_family="Arial",
        layout_title_font=dict(family="Arial", size=24),
        layout_plot_bgcolor="#FFFFFF",
        layout_paper_bgcolor="#FFFFFF",
        layout_showlegend=False,
        layout_xaxis=dict(showgrid=False, zeroline=False),
        layout_yaxis=dict(showgrid=False, zeroline=False),
        layout_font=dict(size=16),
    )

    pio.templates.default = template_name


def load_colorscale(settings_filepath, scale_name="saigreen"):
    """Returns colorscale as list, e.g. from settings.yaml in ci/colorscale/saigreen"""

    with open(settings_filepath) as file:
        settings = yaml.full_load(file)
    try:
        colorscale = settings["ci"]["colorscale"][scale_name]
    except Exception as e:
        logging.error(
            f"Colorscale {scale_name} failed to load from {settings_filepath}. Return empty scale. Error: {e}"
        )
        colorscale = []

    return colorscale
