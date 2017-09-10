# The Movie Db

## Synopsis

This neuron allows you to open an url in an webbrowser

Note: This neuron will only works if you have a GUI.

## Installation
```bash
kalliope install --git-url https://github.com/royto/kalliope_neuron_webbrowser.git
```

### Options

| parameter   | required | type   | default | choices            | comment                        |
|-------------|----------|--------|---------|--------------------|--------------------------------|
| url         | YES      | String | None    |                    | Defines the url to open        |
| option      | NO       | String | None    | current, new, tab  | Option how to open the url     |


### Synapses example

``` yml
  - name: "open-kalliope-github"
    signals:
      - order: "open kalliope github"
    neurons:
      - webbrowser:
          url: "https://github.com/kalliope-project/kalliope"

```

``` yml
  - name: "search-google"
    signals:
      - order: "search for {{ query }} in google"
    neurons:
      - webbrowser:
          url: "https://www.google.fr/search?q={{ query }}"

```

