
# SoundLink

SoundLink is a Python package that provides functionality for recommending music based on certain input.

## Installation

You can install the band_recommendation package using `pip`. Run the following command in your terminal:


```
pip install soundlink
```


## Usage

Here's an example of how to use the SoundLink package in your Python code:

```python
from soundlink import get_band_recommendations, get_song_recommendations

query = 'Pink Floyd'
limit = 10


def main():
    band_recommendations = get_band_recommendations(query, limit)

    '''if you want to get song recommendations from a certain band or artist:'''
    #song_recommendations = get_song_recommendations(query, limit)

if __name__ == '__main__':
    main()

```


Make sure you have a valid Deezer API key to use with the package. You can obtain an API key by creating an account on the Deezer for Developers website.

## Contributing

Contributions to the SoundLink package are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

SoundLink  is released under the MIT License. See the [LICENSE](https://github.com/tudor-Spaima/MusicMap/blob/main/LICENSE "MIT_LICENSE") file for more details.
