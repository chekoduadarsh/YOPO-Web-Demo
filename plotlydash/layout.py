
"""Plotly Dash HTML layout override."""

html_layout = """
<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
        </head>
        <body class="dash-template">
            <header>
              <div class="nav-wrapper">
              <nav class="navbar navbar-light bg-light">
                    <h3>You Only Plot Once - GUI Demo</h3>
                   <a href="https://github.com/chekoduadarsh/YOPO-You-Only-Plot-Once"><i class="fa fa-github" style="font-size:48px;color:black"></i></a>
                </a>
              </nav>
                </br>
                    <h2>CSV Visualizer</h2>
                    </br>
                    <p class="lead">This is a Dash web app which can be used to visualize any CSV. Load the link and Submit!!</p>
                
                <nav>
                </nav>
            </div>
            </header>
            </br>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}

            </footer>
        </body>
    </html>
"""