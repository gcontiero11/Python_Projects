class Species:
    name = ""
    sepal_length = 0
    sepal_width = 0
    petal_length = 0
    petal_width = 0

def Open_file(file_name):
    flowers = []
    arq = open(f"{file_name}" , "r")
    for line in arq:
        data = line.strip().split(",")
        species = Species()
        species.sepal_length = float(data[0])
        species.sepal_width = float(data[1])
        species.petal_length = float(data[2])
        species.petal_width = float(data[3])
        species.name = data[4]
        flowers.append(species)
    arq.close()
    return flowers

def position_biggest_number(arr):
    biggest_number = arr[0]
    position = 0
    for i in range(len(arr)):
        if arr[i] > biggest_number:
            biggest_number = arr[i]
            position = i
    return position

def show_file(arr):
    for elem in arr:
        print(f"Sepal Length: {elem.sepal_length}")
        print(f"Sepal Width: {elem.sepal_width}")
        print(f"Petal Length: {elem.petal_length}")
        print(f"Petal Width: {elem.petal_width}")
        print(f"Name: {elem.name}")

def calculating_distance(flower,list,k):
    minor_distance = []
    species = []
    sepal_l1 = flower.sepal_length
    sepal_w1 = flower.sepal_width
    petal_l1 = flower.petal_length
    petal_w1 = flower.petal_width
    distance = 0
    for elem in list:
        sepal_l2 = elem.sepal_length
        sepal_w2 = elem.sepal_width
        petal_l2 = elem.petal_length
        petal_w2 = elem.petal_width
        distance = ((sepal_l1 - sepal_l2)**2 + (sepal_w1 - sepal_w2)**2 + (petal_l1 - petal_l2)**2 + (petal_w1 - petal_w2)**2) ** (1/2)
        if len(species) < k:
            species.append(elem.name)
            minor_distance.append(distance)
        elif len(species) == k:
            position = position_biggest_number(minor_distance)
            biggest_value = minor_distance[position]
            if distance < biggest_value:
                minor_distance[position] = distance
                species[position] = elem.name
        #print(species)
        #print(minor_distance)
    return species  

def bigger_frequency(arr):
    setosa_count = 0
    versicolor_count = 0
    virginica_count = 0
    #print(arr)
    for elem in arr:
        if elem == 'setosa':
            setosa_count += 1
            #print(f"setosa count: {setosa_count}")
        elif elem == 'versicolor':
            versicolor_count += 1
            #print(f"versicolor count: {versicolor_count}")
        elif elem == 'virginica':
            virginica_count += 1
            #print(f"virginica count: {virginica_count}")
    if setosa_count > versicolor_count and setosa_count > virginica_count:
        return "setosa"
    elif versicolor_count > setosa_count and versicolor_count > virginica_count:
        return "versicolor"
    else:
        return "virginica"

def main():
    species = []
    flowers = Open_file("iris.data.csv")
    k = int(input("K value: "))
    file_name = input("Type the document name:")
    #file_name = "iris.data_2.csv"
    Unknown_species = Open_file(file_name)
    i = 0
    for flower in Unknown_species:
        i += 1
        species = calculating_distance(flower,flowers,k)
        flower.name = bigger_frequency(species)
        print(f"flor {i} : {flower.name}")
main()
