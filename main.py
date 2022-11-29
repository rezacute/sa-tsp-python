# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import googlemaps
import numpy as np
from datetime import datetime
from python_tsp.distances import osrm_distance_matrix
from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.heuristics import solve_tsp_local_search, solve_tsp_simulated_annealing


pd.set_option('mode.chained_assignment', None)


def app_init():
    print("Solving TSP problem with Simulated Annealing Algorithm")
    df = pd.read_csv('data-1.csv')
    df = df.reset_index()

    sources = df[['lat', 'lng']].to_numpy()

    distance_matrix = pd.read_csv("osrm-distance-matrix.csv").to_numpy()
    # Below is the step to get distance matrix from OSRM API
    # distance_matrix = osrm_distance_matrix(
    #     sources,
    #     osrm_server_address="http://router.project-osrm.org",
    #     osrm_batch_size=50,
    # )
    #
    # dm = pd.DataFrame(distance_matrix)
    # dm.to_csv("osrm-distance-matrix.csv",index=False)

    permutation, distance = solve_tsp_simulated_annealing(distance_matrix)

    print("rute",permutation)
    print("distance", distance)
    pd.DataFrame({"route":[permutation],"distance":distance}).to_csv("simulatedannealing-result.csv", index=False)


def sa_result():
    result = np.array([0, 94, 93, 16, 48, 80, 14, 2, 39, 31, 29, 42, 89, 88, 75, 76, 58, 54, 69, 47, 43, 46, 25, 4, 5, 8, 15, 9, 92, 91, 90, 49, 50, 81, 66, 84, 44, 45, 57, 61, 41, 33, 34, 32, 3, 40, 28, 27, 74, 78, 79, 77, 59, 24, 23, 55, 56, 53, 60, 52, 51, 65, 71, 72, 73, 70, 67, 68, 64, 63, 83, 82, 30, 26, 37, 38, 62, 36, 35, 21, 22, 12, 1, 87, 86, 85, 19, 20, 13, 18, 11, 17, 10, 7, 6])
    # rute [0, 6, 7, 8, 9, 11, 18, 16, 17, 13, 12, 1, 87, 86, 85, 19, 20, 21, 22, 62, 39, 3, 32, 31, 88, 89, 57, 79, 76, 78, 74, 75, 33, 34, 29, 28, 27, 40, 38, 2, 36, 35, 26, 30, 50, 49, 48, 90, 91, 92, 15, 5, 4, 94, 93, 45, 51, 52, 53, 54, 58, 23, 77, 41, 42, 61, 56, 60, 68, 67, 64, 72, 69, 71, 73, 70, 65, 80, 84, 14, 82, 83, 81, 66, 43, 44, 46, 25, 10, 37, 59, 24, 55, 63, 47]
    # distance 18607.8

    # rute[
    #     0, 7, 4, 8, 90, 91, 92, 10, 17, 16, 18, 11, 48, 49, 50, 83, 82, 30, 26, 14, 1, 86, 85, 22, 21, 35, 36, 37, 62, 2, 38, 39, 3, 40, 32, 27, 28, 33, 34, 29, 75, 74, 78, 76, 79, 77, 59, 88, 89, 61, 24, 23, 58, 55, 54, 56, 53, 60, 52, 51, 63, 64, 67, 68, 73, 70, 72, 69, 71, 65, 80, 84, 66, 81, 57, 44, 46, 94, 45, 47, 43, 25, 5, 6, 13, 20, 19, 87, 12, 31, 42, 41, 9, 15, 93]
    # distance
    # 16569.8

# this function is to generate latitude and longitude using google maps API
def generate_lat_lng():
    gmaps = googlemaps.Client(key='--Key--')
    df = pd.read_csv('TOUR-19.csv')
    df = df.reset_index()
    df['lat'] = None
    df['lng'] = None

    for index, row in df.iterrows():
        print(row['No.'])

        address = row['No.'] + ' ' + row['Road Name'] + ', Colmar, FRANCE'
        print(address)
        # Geocoding an address
        geocode_result = gmaps.geocode(address)
        df["lat"][index] = geocode_result[0]['geometry']['location']['lat']
        df["lng"][index] = geocode_result[0]['geometry']['location']['lng']
        print(geocode_result[0]['geometry']['location'])

    df.to_csv('out.csv', index=False)


if __name__ == '__main__':
    app_init()


