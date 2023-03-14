#### Flask Installation

pip install Flask

```
### Running flask application
flask --app <filename> run

### Debug
flask --app <filename> run --debug

#### changing host
flask --app <filename> run --host 0.0.0.0 --debug

### changing port 
flask --app <filename> run --host 0.0.0.0 --port <whatever port we wants to use> --debug

```

- app.route (binding of relative url with functions)

NOTE : MVC
- Model :- It represents resource like (database)
- View  :- whatever we see on the ui
- Control :- This is about backend