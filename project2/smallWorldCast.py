def getConnections(cast):
    try:
        # check if the first two casts have any actors in common
        if set(cast[0]) & set(cast[1]):
            intersect = set(cast[0]) & set(cast[1])
            outputtext =""
            if len(intersect) == 1:
                outputtext = "actor"
            else:
                outputtext = "cast"
            # if so return the intersection
            return f'Shortest Connection = 1, {outputtext} = {set(cast[0]) & set(cast[1])}'
        else:
            # else for each remaining cast i, check if there is any intersection between cast 0 and i and cast 1 and i
            for i in cast:
                if set(cast[0]) & set(i) and set(cast[1]) & set(i):
                    return f'Shortest connection = 2, cast = {set(i)}'
            return f'shortest connection > 2 or no connection'
    except:
        return "Something went wrong please try again by refining the inputs accoring to the constraints"

if __name__ == "__main__":
    # please provide input in the input cast text file, each input should be of the following format,
    # first line should be the number of casts , followed by comma separeted names of the cast in each new line
    file = open('inputcast.txt')
    while True:
        # read the number of casts for first example
        numberOfCasts = file.readline()
        cast = []
        if numberOfCasts:
            # create a 2D array for storing each casts
            cast = [[]] * int(numberOfCasts)
            for i in range(int(numberOfCasts)):
                # read new cast on new line and separte them based on comma ","
                cast[i] = list(map(str.strip,file.readline().lstrip().split(',')))
            # for each input example call the getConnection function and print the resuly
            print(getConnections(cast))
        else:
            break
