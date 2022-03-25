# ***************************************
# Imports
# ***************************************
# Dash
import dash
from dash import html
from dash import dcc

# Plotly
import plotly.express as px

# ***************************************
# Get data
# ***************************************
import Delivery1
order = Delivery1.get_data()

# ***************************************
# Diagram - Employee Sales
# ***************************************
fig_employee = px.bar(order,
    x='emp_name', y='total',
    color='type', text='total', title='Salg pr medarbejder',
    hover_data=[],
    labels={'total':'Samlede salg', 'emp_name':'Medarbejder'})
fig_employee.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_employee.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=45)

# ***************************************
# Diagram - Employee Sales
# ***************************************
fig_product = px.bar(order,
    x='productname', y='total',
    color='type', text='total', title='Sales by Product',
    hover_data=[],
    labels={'total':'Samlede salg', 'product_name':'productname', 'type':'Produkt type'})
fig_product.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_product.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=45)


# ***************************************
# Activate the app
# ***************************************
#app = dash.Dash(__name__)

dash_app = dash.Dash(__name__)
app = dash_app.server

# ***************************************
# Layout
# ***************************************
dash_app.layout = html.Div(
    children=[
        html.Div(className='row',
                children=[
                    html.Div(className='four columns div-user-controls',
                            children=[
                                html.H2('Salgs dashboard')]),

                        
                    html.Div(className='eight columns div-for-charts bg-grey',
                            children=[
                                dcc.Graph(id="sales_employee", figure=fig_employee),
                                dcc.Graph(id="product_name", figure=fig_product),
                                    ]
                            ),

                        ]
                    )
                ]
)


# ***************************************
# Run the app
# ***************************************
if __name__ == '__main__':
    dash_app.run_server(debug=True)
