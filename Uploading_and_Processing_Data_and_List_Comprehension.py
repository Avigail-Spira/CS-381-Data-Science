{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Uploading and Processing Data and List Comprehension  ",
      "provenance": [],
      "authorship_tag": "ABX9TyPHeOlCDql7JFKgnuYsS8KH",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Avigail-Spira/CS-381/blob/main/Uploading_and_Processing_Data_and_List_Comprehension.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np"
      ],
      "metadata": {
        "id": "w-IQ64OP2NQ5"
      },
      "execution_count": 47,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv(\"https://raw.githubusercontent.com/Avigail-Spira/CS-381/main/cars-sample35.txt\")\n",
        "\n",
        "#Set the columns\n",
        "df.columns = ['price', 'maintenanceCost', 'numberOfDoors', 'numberOfPassengers', 'luggageCapacity', 'safetyRating', 'classificationOfVehicle']\n",
        "print(df)\n",
        "\n",
        "price = list(df['price'])\n",
        "maintenanceCost = list(df['maintenanceCost'])\n",
        "numberOfDoors = list(df['numberOfDoors'])\n",
        "numberOfPassengers = list(df['numberOfPassengers'])\n",
        "luggageCapacity = list(df['luggageCapacity'])\n",
        "safetyRating = list(df['safetyRating'])\n",
        "classificationOfVehicle = list(df['classificationOfVehicle'])"
      ],
      "metadata": {
        "id": "j4SQvaaUE-bi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#####Find the list index values of each automobile having a “price” rating of \"med\""
      ],
      "metadata": {
        "id": "k6FwY38-XeZ0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "cond1 = list(df.index[df['price'] == 'med'])\n",
        "print(cond1)"
      ],
      "metadata": {
        "id": "KNpgBeNeXp1j"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "####Find the \"number of passengers\" value for each auto having a \"price\" value of \"med\"\n"
      ],
      "metadata": {
        "id": "fwxaV_19Xk7d"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "cond2 = list(df[df['price'] == 'med']['numberOfPassengers'])\n",
        "print(cond2)"
      ],
      "metadata": {
        "id": "itVFpT2uXr03"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "####Find the index value for each automobile having a “price” value of \"high\" and a “maintenance” value that is not \"low\".\n"
      ],
      "metadata": {
        "id": "3LrglyM9XnnP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "cond3 = np.where((df['price'] == 'high') & (df['maintenanceCost'] != 'low'))\n",
        "print(cond3)"
      ],
      "metadata": {
        "id": "5AiLdlljXvTd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "####Find the list index values of each automobile having a price rating of \"med using a list comprehension instead of a basic for or while loop\n"
      ],
      "metadata": {
        "id": "kWJwjr83XoFX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "cond4 = [i for i, val in enumerate(df['price']) if val == 'med']\n",
        "print(cond4)"
      ],
      "metadata": {
        "id": "gs310vAtX2qv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "####Find the \"number of passengers\" value for each auto having a \"price\" value of \"med\" using a list comprehension instead of a basic for or while loop."
      ],
      "metadata": {
        "id": "LDdLtANWXoLa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "cond5 = [df['numberOfPassengers'][i] for i,val in enumerate(df['price']) if val == 'med']\n",
        "print(cond5)"
      ],
      "metadata": {
        "id": "bMiAA2mdX72r"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "####Find the index value for each automobile having a price value of \"high\" and a maintenance value that is not \"low\" using a list comprehension\n"
      ],
      "metadata": {
        "id": "G5w64EheX99n"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "cond6 = [i for i, val in enumerate(df['price']) for i, val2 in enumerate(df['maintenanceCost']) if val == 'high' and val2 != 'low']\n",
        "print(cond6)"
      ],
      "metadata": {
        "id": "BPFv7pojYAYP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "####Consider the following list of lists: nlist = [ [1, 2, 3], [‘A’, ‘B’, ‘C’], [4, 5], [‘D’, ‘E’] ]. Extract each individual element of the component lists contained within nlist and add them to a new list.  Do NOT use a nested for loop, use a list comprehension.\n"
      ],
      "metadata": {
        "id": "itt6pbOZYDSs"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "a2VID4B02Kyi"
      },
      "outputs": [],
      "source": [
        "nlist = [[1, 2, 3], ['A', 'B', 'C'], [4, 5], ['D', 'E']]\n",
        "flattenedList = [i for sublist in nlist for i in sublist]\n",
        "print(flattenedList)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Nested List Comprehension\n",
        "###Consider the following list of lists: nlist = [ [1, 2, 3], [‘A’, ‘B’, ‘C’], [4, 5], [‘D’, ‘E’] ]. Extract each individual element of the component lists contained within nlist and add them to a new list.  Do NOT use a nested for loop, use a list comprehension.\n"
      ],
      "metadata": {
        "id": "csJp_wssXCkF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "nlist = [[1, 2, 3], ['A', 'B', 'C'], [4, 5], ['D', 'E']]\n",
        "flattenedList = [i for sublist in nlist for i in sublist]\n",
        "print(flattenedList)"
      ],
      "metadata": {
        "id": "sLl-bOXlXTsi"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}