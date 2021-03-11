library(shiny)
library(SentimentAnalysis)
library(multcompView)
library(dplyr)
library(DT)
library(ggplot2)
library(shiny)

Disney <- read.csv("Disney.csv", stringsAsFactors = T)
names(Disney) <- c("Title", "ReleaseDate", "Genre","Rating", 
                   "Gross","Inflation")
Netflix<- read.csv("netflix.csv", stringsAsFactors = T)


# Define UI for application that draws a histogram
ui <- navbarPage("Movie Time",
                 tabPanel("Netflix vs. Disney",
                          h6("Whether it's Drama, Action, Comedy, Thriller or
    Romance this collection of famous movie datasets can 
    be appreciated by any lover of cinema."),
                          textInput(inputId = "caption",
                                    label = "Caption:",
                                    value = "Data Summary"),
                          selectInput(inputId = "dataset",
                                      label = "Choose a dataset:",
                                      choices = c("Disney","Netflix")),
                          numericInput(inputId = "obs",
                                       label = "Number of observations to view:",
                                       value = 5),
                          verbatimTextOutput("summary"),
                          tableOutput("view")),
                 tabPanel("Disney Plot", h6("This visual shows Disney movie genres, and how much each genre has made from 1937 to 2016. This visual reveals that the genre Adventure is the most popular Disney movie genre. The visual also reveals that Adventure movies have made over 15B dollars. Some of the most popular Disney Adventure movies include Star Wars, Rogue One, Lion King, Alice in Wonderland, and Pirates of the Caribbean. If Disney wants to continue to increase total gross they should focus on creating more Action, Comedy, and Adventure movies since these genres are mostly preferred by viewers."),
                          plotOutput("g1")
                          ),
                tabPanel("Netflix Plot", h6("This visual shows the number of movies and tv shows that were relased on the Netlfix app by rating. This Netflix data reaveals that TV-MA is the most popular rating on Netflix with over 1750 movies and over 1000 tv shows with this rating. If Netflix wanted to reach a wider audience range they could increase subscriptions and profit by including more family friendly content on the app. This includes increasing the number of G, PG and PG-13 ratings. It is likely that a user will subscribe to another platform like Disney+ for these particular movies."),
                         plotOutput("g2")
                         ),
                tabPanel("Netflix Movie/TV Search", dataTableOutput("g3")
                         ),
                tabPanel("Disney Movie Search", dataTableOutput("g4")
                         ))
                

       
# Define server logic required to draw a histogram
server <- function(input, output) {

    datasetInput <- reactive({
        switch(input$dataset,
               "Disney" = Disney,
               "Netflix" = Netflix)
    })
    
    
    output$caption <- renderText({
        input$caption
    })
    
    
    output$summary <- renderPrint({
        dataset <- datasetInput()
        summary(dataset)
    })
    
    
    output$view <- renderTable({
        head(datasetInput(), n = input$obs)
    })


output$g1 <- renderPlot({
    ggplot(Disney, aes(x= Genre, y = Gross, fill = Genre))+
               geom_bar(stat = "identity")+
               scale_x_discrete(guide = guide_axis(n.dodge=3))
               
})

output$g2 <- renderPlot({
    ggplot(Netflix, aes(type, ..count..))+
    geom_bar(aes(fill = rating), position = "dodge")
        
})
output$g3 <- renderDataTable({
     Netflix
})

output$g4 <- renderDataTable({
     Disney
    
})
}
# Run the application 
shinyApp(ui = ui, server = server)
