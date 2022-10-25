import streamlit as st

class Bus:
    def Conductor(self):
        # return 'Soumyajit Mitra'
        return name

    def Speed(self):
        # return 50
        return speed

    def Capacity(self):
        # return 75
        return capacity

    def fare(self):
        # return 10
        return fare


class stations:
    def dist(self):
        # return 20
        return dist

    def stops(self):
        return 13


Bus1 = Bus()
Station = stations()

passengers = [15, 22, 21, 11, 16, 26, 19, 18, 13, 6, 15, 5, 12, 7]

st.header('Bus Conductor Helper')

name = st.text_input("Enter the name of Bus Conductor :-")
speed = st.number_input('Provide the average speed of the bus in kmph :-', value=0, step=1)
capacity = st.number_input('Provide the total capacity (excluding the driver and the conductor) of the bus in :-', value=0, step=1)
fare = st.number_input('Enter the amount of fare for riding the bus :-', value=0, step=1)
dist = st.number_input('Provide the average distance between each bus stop in km:-', value=0, step=1)

if st.button('Submit') :
    s = 0
    i = 1
    total = 0
    for x in passengers:
        s = s + (x)
        if s <= Bus1.Capacity():
            # print("The bus picked",(x),"people from station",i)
            st.write('The bus picked', x, 'people from staion', i)
            i += 1
            total = s


    # print("The bus picked",(Bus1.Capacity() - total),"people from station",i,)
    st.write("The bus picked", Bus1.Capacity() - total, "people from station", i,)
    
    if (s >= Bus1.Capacity()):
        # print("The bus got completely filled.")
        st.write("The bus got completely filled.")

        l = s - Bus1.Capacity()
        # print("Number of passengers the bus wont be able to pick",l,"people.")
        st.write("Number of passengers the bus wont be able to pick ", l, " people.")

    # print("The minimum duration for which the bus drives until it gets filled is",Station.dist()*(i-1)/Bus1.Speed(),"hr.")
    st.write("The minimum duration for which the bus drives until it gets filled is ",Station.dist()*(i-1)/Bus1.Speed(), "hr.")

    # print(Bus1.Conductor(),"and his total earnings would be", Bus1.fare()*Bus1.Capacity(),"Rs.")
    st.write(Bus1.Conductor(), " is the conductor of the bus and his total earnings would be ",Bus1.fare()*Bus1.Capacity(), " Rs.")
