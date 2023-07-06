from dash.dependencies import Output, Input
import dash
import dash_core_components as dcc
import dash_html_components as html
from pages import mediciones_page
from pages import inicio_page 
from pages import informe_tecnico_page
from pages import informe_legal_page


external_scripts_dict = [
    {
        "src": "https://kit.fontawesome.com/d147d1adc0.js",
        "crossorigin": "anonymous"
    }
]

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_scripts=external_scripts_dict)

# Definir el estilo CSS para los contenedores principales
app.layout = html.Div(className="main-container",
    children=[
        dcc.Location(id='url', refresh=False),
        # Menú
        html.Div(
            children=[
                html.H2(dcc.Link('Proyecto ANE', href='/')),
                html.Ul([
                    html.Li([html.I(className="fa-solid fa-timeline"),dcc.Link('Línea de tiempo', href='/linea-de-tiempo')]),
                    html.Li([html.I(className="fa-solid fa-chart-line"),dcc.Link('Mediciones', href='/mediciones')]),
                    html.Li([html.I(className="fa-solid fa-chart-line"),dcc.Link('Simulaciones', href='/simulaciones')]),
                    html.Li([html.I(className="fa-solid fa-file-pdf"),dcc.Link('Informe técnico', href='/informe-tecnico')]),
                    html.Li([html.I(className="fa-solid fa-file-pdf"),dcc.Link('Informe legal', href='/informe-legal')]),
                    html.Li([html.I(className="fa-solid fa-file"),dcc.Link('Archivos', href='/archivos')]),
                    html.Div(className="active")
                ], className="nav-links")
            ], className="menu-container"
        ),
        # Contenido dinámico
        html.Div(
            id='content',
            children=[
                html.H2('Bienvenido'),
                html.P('Selecciona una opción del menú para ver el contenido correspondiente.')
            ], className="content-container"
        )
    ]
)

app._favicon = ("assets\favicon.ico")


@app.callback(
    Output('content', 'children'),
    [Input('url', 'pathname')]
)
def display_content(pathname):
    if pathname == '/mediciones':
        return mediciones_page.layout()
    elif pathname == '/simulaciones':
        return html.Div([
            html.H2('Simulaciones'),
            # contenido
        ])
    elif pathname == '/informe-tecnico':
        return informe_tecnico_page.layout()
        # return html.Div([
        #     html.H2('Informe técnico'),
        #     # contenido
        # ])
    elif pathname == '/informe-legal':
        return informe_legal_page.layout()
        # return html.Div([
        #     html.H2('Informe legal'),
        #     # contenido
        # ])
    elif pathname == '/archivos':
        return html.Div([
            html.H2('Archivos'),
            # contenido
        ])
    elif pathname == '/linea-de-tiempo':
        return html.Div([
            html.H2('Línea de tiempo'),
            # contenido
        ])
    else:
        return inicio_page.layout()



if __name__ == '__main__':
    mediciones_page.register_callbacks(app)
    app.run_server(debug=True)