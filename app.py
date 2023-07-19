from dash.dependencies import Output, Input
import dash
from dash import dcc
from dash import html
from pages import mediciones_page
from pages import inicio_page
from pages import informe_tecnico_page
from pages import informe_legal_page
from pages import informe_final_page
from pages import archivos_page
from pages import linea_de_tiempo_page


external_scripts_dict = [
    {
        "src": "https://kit.fontawesome.com/d147d1adc0.js",
        "crossorigin": "anonymous"
    }
]

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_scripts=external_scripts_dict)


# Definir el estilo CSS para los contenedores principales
app.layout = html.Div(className="main-container",
                      children=[
                          dcc.Location(id='url', refresh=False),
                          html.Header(
                              html.Div(html.I(className="fa-solid fa-bars"),
                                       className="icon-menu")
                          ),
                          # Menú
                          html.Div(
                              children=[
                                  html.Div(
                                      [
                                          html.I(
                                              className="fa-solid fa-house"),
                                          html.H3(
                                              dcc.Link('Proyecto ANE', href='/'))
                                      ],
                                      className="page-title"
                                  ),
                                  html.Div([
                                      html.A(href='/linea-de-tiempo', className="selected", children=[
                                          html.Div([
                                              html.I(className="fa-solid fa-timeline", title="Línea de tiempo"),
                                              html.H4("Línea de tiempo")
                                          ], className="opt")
                                      ]),
                                      html.A(href='/mediciones', children=[
                                          html.Div([
                                              html.I(className="fa-solid fa-chart-line", title="Mediciones"),
                                              html.H4("Mediciones")
                                          ], className="opt")
                                      ]),
                                      html.A(href='/simulaciones', children=[
                                          html.Div([
                                              html.I(className="fa-solid fa-chart-line", title="Simulaciones"),
                                              html.H4("Simulaciones")
                                          ], className="opt")
                                      ]),
                                      html.A(href='/informe-tecnico', children=[
                                          html.Div([
                                              html.I(className="fa-solid fa-file-pdf", title="Informe técnico"),
                                              html.H4("Informe técnico")
                                          ], className="opt")
                                      ]),
                                      html.A(href='/informe-legal', children=[
                                          html.Div([
                                              html.I(className="fa-solid fa-file-pdf", title="Informe legal"),
                                              html.H4("Informe legal")
                                          ], className="opt")
                                      ]),
                                      html.A(href='/informe-final', children=[
                                          html.Div([
                                              html.I(className="fa-solid fa-file-pdf", title="Informe final"),
                                              html.H4("Informe final")
                                          ], className="opt")
                                      ]),
                                      html.A(href='/archivos', children=[
                                          html.Div([
                                              html.I(className="fa-solid fa-file", title="Archivos"),
                                              html.H4("Archivos")
                                          ], className="opt")
                                      ]),
                                  ],
                                      className="opts-menu"
                                  )
                                  # html.Div(children=[
                                  #     html.Div(className="hamburguer")
                                  # ],className="menu-toggle"),
                                  # html.Ul([
                                  #     html.Li([html.I(className="fa-solid fa-timeline"),dcc.Link('Línea de tiempo', href='/linea-de-tiempo')]),
                                  #     html.Li([html.I(className="fa-solid fa-chart-line"),dcc.Link('Mediciones', href='/mediciones')]),
                                  #     html.Li([html.I(className="fa-solid fa-chart-line"),dcc.Link('Simulaciones', href='/simulaciones')]),
                                  #     html.Li([html.I(className="fa-solid fa-file-pdf"),dcc.Link('Informe técnico', href='/informe-tecnico')]),
                                  #     html.Li([html.I(className="fa-solid fa-file-pdf"),dcc.Link('Informe legal', href='/informe-legal')]),
                                  #     html.Li([html.I(className="fa-solid fa-file-pdf"),dcc.Link('Informe final', href='/informe-final')]),
                                  #     html.Li([html.I(className="fa-solid fa-file"),dcc.Link('Archivos', href='/archivos')]),
                                  #     html.Div(className="active")
                                  # ], className="nav-links menu")
                              ], className="menu-container"
                          ),
                          # Contenido dinámico
                          html.Div(
                              id='content',
                              children=[
                                  html.H2('Bienvenido'),
                                  html.P(
                                      'Selecciona una opción del menú para ver el contenido correspondiente.')
                              ], className="content-container container"
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
        ])
    elif pathname == '/informe-tecnico':
        return informe_tecnico_page.layout()
    elif pathname == '/informe-legal':
        return informe_legal_page.layout()
    elif pathname == '/informe-final':
        return informe_final_page.layout()
    elif pathname == '/archivos':
        return archivos_page.layout()
    elif pathname == '/linea-de-tiempo':
        return linea_de_tiempo_page.layout()
    else:
        return inicio_page.layout()


if __name__ == '__main__':
    mediciones_page.register_callbacks(app)
    archivos_page.register_callbacks(app)
    linea_de_tiempo_page.register_callbacks(app)
    app.run_server(debug=True)
