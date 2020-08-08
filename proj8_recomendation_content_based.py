import paho.mqtt.client as mqtt
import numpy as np
from matplotlib import pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import datetime
import pandas as pd
import time

#filter
# https://gist.github.com/junzis/e06eca03747fc194e322
from scipy.signal import butter, lfilter, freqz
# Filter requirements.
order = 3
fs = 30.0       # sample rate, Hz
cutoff = 4 # desired cutoff frequency of the filter, Hz

alpha = 0.5
index_filterx = 1
index_filtery = 1
index_filterz = 1
AxFilter=[0] * 10
AyFilter=[0] * 10
AzFilter=[0] * 10

# figure

#fig = plt.gcf()
#fig.show()
#fig.canvas.draw()

#plt.ion()

topic_device_1 = "Device1/"
topic_accX = "accX"
topic_accY = "accY"
topic_accZ = "accZ"
topic_flex1 = "flex1"
topic_flex2 = 'flex2'


# integral sampling time
dt = 0.01
vX = 0
vZ = 0
positionX = 0
positionZ = 0


# low pass
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

# low pass
def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


# calculate integration of accleration
def double_integration_acc(listAcc,deltaTime=dt):
    '''
        listAcc = array of accelerometer
        deltaTime = sampling time, defaut value 0.001 / 1ms

        return
            position, velocity
    '''
    velocity = []
    velocity.append(0) # add first element of velocity = 0
    position = []
    position.append(0) # add first element of position = 0

    # first integration
    for i in range(len(listAcc)):
        #result += x * deltaTime # integral
        vel_now = velocity[i] + listAcc[i] * deltaTime
        velocity.append(vel_now) # velcocity = prev_velocity + current_accleration*deltaTime

    # double integration
    for i in range(len(velocity)):
        position_now = position[i] + velocity[i] * deltaTime
        position.append(position_now) # position = prev_position + current_velocity*deltaTime

    # sum all element
    return abs(np.sum(position)) , abs(np.sum(velocity))

# csvwrite
def write_tocsv(topic,dataframe) :
    """
    Write result data to csv file
    :param data:dataSaved as dataframe
    :return:
    """
    global filename
    csvfilename = filename.replace('devicename',topic)
    dataframe.to_csv(csvfilename, mode='a', header=False,index=False)

def preprocessing(data_str):
    split_data = data_str.split(",")
    data_float = np.array(split_data).astype(np.float) # convert array of string to array of float
    result = data_float
    return result

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic_device_1+"#")
    client.subscribe(topic_device_2+"#")
    client.subscribe(topic_device_3+"#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # 1. Terima data AccX,AccY,AccZ
    # 2. Preprocessing
    # 3. LPF
    # 4. Integral
    # 5. Fuzzy
    '''
    '''
    global decision, vX, vZ, fuzzLongsor, positionX, positionZ
    print("----------------------------------------------- \n")
    # device 1
    if(msg.topic == topic_device_1+topic_accX):
        device_name = msg.topic.split("/")[0]
        print(device_name)
        print("-------------------------------")
        print(topic_device_1 + "AccX")
        # 1
        data_raw = str(msg.payload)
        # 2
        data_float = preprocessing(data_raw)
        print("RAW Data ")
        print(data_float)
        # 3
        filtered_data = butter_lowpass_filter(data_float, cutoff, fs, order)
        print("LPF AccX : ")
        print(filtered_data)

        '''
        data_filtered_2 = []
        for val in data_float:
            AxFilter[index_filterx]=alpha * val +(1-alpha) * AxFilter[index_filterx-1]
            AxFilter[index_filterx-1]=AxFilter[index_filterx]
            AxFiltered=AxFilter[index_filterx]
            data_filtered_2.append(AxFiltered)

        print("Data Filtered 2 : ")
        print(data_filtered_2)


        velocityX = 0
        for x in data_filtered_2:
            velocityX += x * dt # integral
        '''

        # 4
        #velocity, position = double_integration(data_filtered_2,data_filtered_2,data_filtered_2)
        vX, positionX = double_integration_acc(filtered_data)
        print("Velocity X  : ")
        print(vX)
        print("Position X : ")
        print(positionX)
    elif(msg.topic == topic_device_1+topic_accZ):
        device_name = msg.topic.split("/")[0]
        print(device_name)
        print(topic_device_1 + " AccZ ")
        # 1
        data_raw = str(msg.payload)
        # 2
        data_float = preprocessing(data_raw)
        # 3
        filtered_data = butter_lowpass_filter(data_float, cutoff, fs, order)
        print("LPF AccZ : ")
        print(filtered_data)

        #vZ = velocityZ
        vZ, positionZ = double_integration_acc(filtered_data)

        print("Velocity X  : ")
        print(vX)
        print("Position X : ")
        print(positionX)
        print("Velocity Z  : ")
        print(vZ)
        print("Position Z : ")
        print(positionZ)

        # fuzzy input
        decision.input['Position Z'] = positionZ
        decision.input['Position X'] = positionX
        decision.compute()
        print("Decision : ")
        decision_result = decision.output['Longsor']
        if(decision_result > 50):
            decision_result_str = "Ya Longsor"
        else:
            decision_result_str = "Tidak Longsor"
        print('Value : {} - Status : {}'.format(decision_result,decision_result_str))


        # save to csv
        saved_csv = []
        saved_csv.append(int(time.time()))
        saved_csv.append(positionX)
        saved_csv.append(positionZ)
        saved_csv.append(decision_result)
        saved_csv.append(decision_result_str)
        dataSaved = pd.DataFrame([saved_csv])
        write_tocsv(device_name,dataSaved)

    # device 2
    elif(msg.topic == topic_device_2+topic_accX):
        device_name = msg.topic.split("/")[0]
        print(device_name)
        # receive data
        print(topic_device_2 + " AccX")
        # 1
        data_raw = str(msg.payload)
        # 2
        data_float = preprocessing(data_raw)
        print("RAW Data ")
        print(data_float)
        # 3
        filtered_data = butter_lowpass_filter(data_float, cutoff, fs, order)
        print("LPF AccX : ")
        print(filtered_data)

        '''
        data_filtered_2 = []
        for val in data_float:
            AxFilter[index_filterx]=alpha * val +(1-alpha) * AxFilter[index_filterx-1]
            AxFilter[index_filterx-1]=AxFilter[index_filterx]
            AxFiltered=AxFilter[index_filterx]
            data_filtered_2.append(AxFiltered)

        print("Data Filtered 2 : ")
        print(data_filtered_2)


        velocityX = 0
        for x in data_filtered_2:
            velocityX += x * dt # integral
        '''

        # 4
        #velocity, position = double_integration(data_filtered_2,data_filtered_2,data_filtered_2)
        vX, positionX = double_integration_acc(filtered_data)
        print("Velocity X  : ")
        print(vX)
        print("Position X : ")
        print(positionX)
    elif(msg.topic == topic_device_2+topic_accZ):
        device_name = msg.topic.split("/")[0]
        print(device_name)
        print(topic_device_2 + " AccZ ")
        # 1
        data_raw = str(msg.payload)
        # 2
        data_float = preprocessing(data_raw)
        # 3
        filtered_data = butter_lowpass_filter(data_float, cutoff, fs, order)
        print("LPF AccZ : ")
        print(filtered_data)

        #vZ = velocityZ
        vZ, positionZ = double_integration_acc(filtered_data)

        print("Velocity X  : ")
        print(vX)
        print("Position X : ")
        print(positionX)

        print("Velocity Z  : ")
        print(vZ)
        print("Position Z : ")
        print(positionZ)

        # fuzzy input
        decision.input['Position Z'] = positionZ
        decision.input['Position X'] = positionX
        decision.compute()
        print("Decision : ")
        decision_result = decision.output['Longsor']
        if(decision_result > 50):
            decision_result_str = "Ya Longsor"
        else:
            decision_result_str = "Tidak Longsor"
        print('Value : {} - Status : {}'.format(decision_result,decision_result_str))

        # save to csv
        saved_csv = []
        saved_csv.append(int(time.time()))
        saved_csv.append(positionX)
        saved_csv.append(positionZ)
        saved_csv.append(decision_result)
        saved_csv.append(decision_result_str)
        dataSaved = pd.DataFrame([saved_csv])
        write_tocsv(device_name,dataSaved)

    # device 3
    elif(msg.topic == topic_device_3+topic_accX):
        device_name = msg.topic.split("/")[0]
        print(device_name)
        print(topic_device_3 + " AccX")
        # 1
        data_raw = str(msg.payload)
        # 2
        data_float = preprocessing(data_raw)
        print("RAW Data ")
        print(data_float)
        # 3
        filtered_data = butter_lowpass_filter(data_float, cutoff, fs, order)
        print("LPF AccX : ")
        print(filtered_data)

        '''
        data_filtered_2 = []
        for val in data_float:
            AxFilter[index_filterx]=alpha * val +(1-alpha) * AxFilter[index_filterx-1]
            AxFilter[index_filterx-1]=AxFilter[index_filterx]
            AxFiltered=AxFilter[index_filterx]
            data_filtered_2.append(AxFiltered)

        print("Data Filtered 2 : ")
        print(data_filtered_2)


        velocityX = 0
        for x in data_filtered_2:
            velocityX += x * dt # integral
        '''

        # 4
        #velocity, position = double_integration(data_filtered_2,data_filtered_2,data_filtered_2)
        vX, positionX = double_integration_acc(filtered_data)
        print("Velocity X  : ")
        print(vX)
        print("Position X : ")
        print(positionX)
    elif(msg.topic == topic_device_3+topic_accZ):
        device_name = msg.topic.split("/")[0]
        print(device_name)
        print(topic_device_3 + " AccZ ")
        # 1
        data_raw = str(msg.payload)
        # 2
        data_float = preprocessing(data_raw)
        # 3
        filtered_data = butter_lowpass_filter(data_float, cutoff, fs, order)
        print("LPF AccZ : ")
        print(filtered_data)


        velocityZ = 0
        for x in filtered_data:
            velocityZ += x * dt # integral

        #vZ = velocityZ
        vZ, positionZ = double_integration_acc(filtered_data)

        print("Velocity X  : ")
        print(vX)
        print("Position X : ")
        print(positionX)

        #
        print("Velocity Z  : ")
        print(vZ)
        print("Position Z : ")
        print(positionZ)

        # fuzzy input
        decision.input['Position Z'] = positionZ
        decision.input['Position X'] = positionX
        decision.compute()
        print("Decision : ")
        decision_result = decision.output['Longsor']
        if(decision_result > 50):
            decision_result_str = "Ya Longsor"
        else:
            decision_result_str = "Tidak Longsor"
        print('Value : {} - Status : {}'.format(decision_result,decision_result_str))

        # save to csv
        saved_csv = []
        saved_csv.append(int(time.time()))
        saved_csv.append(positionX)
        saved_csv.append(positionZ)
        saved_csv.append(decision_result)
        saved_csv.append(decision_result_str)
        dataSaved = pd.DataFrame([saved_csv])
        write_tocsv(device_name,dataSaved)


def on_log(mqttc, obj, level, string):
    print(string)


if __name__== '__main__':
    dt = datetime.datetime.now()
    filename = 'result/%s-%s-%s-%s-%s.csv' % ("devicename", dt.day, dt.month, dt.year, dt.hour)
    print(filename)
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    #client.on_log = on_log

    server_broker = "127.0.0.1"
    client.connect(server_broker, 1883, 60)

        # fuuzzy
    '''
    * Antecednets (Inputs)
    - `Velocity X`
        * Universe (ie, crisp value range): on a scale of 0 to 10?
        * Fuzzy set (ie, fuzzy value range): dekat, sedang, jauh
    - `Velocity Z`
        * Universe: How tasty was the food, on a scale of 0 to 10?
        * Fuzzy set: dekat, sedang, jauh
    * Consequents (Outputs)
    - `Longsor`
        * Universe: on scale 0 .. 1
        * Fuzzy set: tidak, ya
    * Rules
    - IF the *service* was good  *or* the *food quality* was good,
        THEN the tip will be high.
    - IF the *service* was average, THEN the tip will be medium.
    - IF the *service* was poor *and* the *food quality* was poor
        THEN the tip will be low.
    * Usage
    - If I tell this controller that I rated:
        * the service as 9.8, and
        * the quality as 6.5,
    - it would recommend I leave:
        * a 20.2% tip.
    '''
    fuzzPositionX = ctrl.Antecedent(np.arange(0, 11, 1), 'Position X') # 0 .. 10
    fuzzPositionZ = ctrl.Antecedent(np.arange(0, 11, 1), 'Position Z') # 0 .. 10
    fuzzLongsor = ctrl.Consequent(np.arange(0,101,1) , 'Longsor') # 0 .. 1

    # membership function position X
    fuzzPositionX['dekat'] = fuzz.trimf(fuzzPositionX.universe , [0,0,3])
    fuzzPositionX['sedang'] = fuzz.trapmf(fuzzPositionX.universe,[2,4,6,8])
    fuzzPositionX['jauh'] = fuzz.trimf(fuzzPositionX.universe, [7,10,10])

    # membership function position Z
    fuzzPositionZ['dekat'] = fuzz.trimf(fuzzPositionZ.universe , [0,0,3])
    fuzzPositionZ['sedang'] = fuzz.trapmf(fuzzPositionZ.universe,[2,4,6,8])
    fuzzPositionZ['jauh'] = fuzz.trimf(fuzzPositionZ.universe, [7,10,10])

    # membership function longsor
    fuzzLongsor['tidak'] = fuzz.trapmf(fuzzLongsor.universe, [0,0,45,55])
    fuzzLongsor['ya'] = fuzz.trapmf(fuzzLongsor.universe, [45,55,100,100])

    # show
    fuzzPositionX.view()
    fuzzPositionZ.view()
    fuzzLongsor.view()

    # rule
    '''
    Fuzzy rules
    -----------

    Now, to make these triangles useful, we define the *fuzzy relationship*
    between input and output variables. For the purposes of our example, consider
    three simple rules:

    1. If the velocityX is dekat OR the dekat, then the tip will be low

    '''
    rule1 = ctrl.Rule(fuzzPositionX['dekat'] | fuzzPositionZ['dekat'], fuzzLongsor['tidak'])
    rule2 = ctrl.Rule(fuzzPositionX['jauh'] | fuzzPositionZ['jauh'], fuzzLongsor['ya'])
    rule3 = ctrl.Rule(fuzzPositionZ['sedang'] | fuzzPositionX['sedang'], fuzzLongsor['ya'])
    rule4 = ctrl.Rule(fuzzPositionZ['sedang'] & fuzzPositionX['dekat'], fuzzLongsor['tidak'])
    rule5 = ctrl.Rule(fuzzPositionZ['dekat'] & fuzzPositionX['sedang'], fuzzLongsor['tidak'])

    rule6= ctrl.Rule(fuzzPositionX['dekat'] | fuzzPositionZ ['jauh'], fuzzLongsor['tidak'])
    rule7= ctrl.Rule(fuzzPositionX['dekat'] | fuzzPositionZ ['sedang'], fuzzLongsor['tidak'])
    rule8= ctrl.Rule(fuzzPositionX['jauh'] & fuzzPositionZ ['sedang'], fuzzLongsor['ya'])
    rule9= ctrl.Rule(fuzzPositionX['jauh'] | fuzzPositionZ ['dekat'], fuzzLongsor['tidak'])
    rule10= ctrl.Rule(fuzzPositionX['sedang'] & fuzzPositionZ ['sedang'], fuzzLongsor['ya'])
    rule11= ctrl.Rule(fuzzPositionX['sedang'] & fuzzPositionZ ['jauh'], fuzzLongsor['ya'])
    rule12= ctrl.Rule(fuzzPositionX['sedang'] & fuzzPositionZ ['dekat'], fuzzLongsor['tidak'])

    rule13 = ctrl.Rule(fuzzPositionZ['dekat'] & fuzzPositionX['dekat'], fuzzLongsor['tidak'])
    rule14= ctrl.Rule(fuzzPositionZ['dekat'] & fuzzPositionX['sedang'], fuzzLongsor['tidak'])
    rule15 = ctrl.Rule(fuzzPositionZ['dekat'] & fuzzPositionX['jauh'], fuzzLongsor['tidak'])
    rule16 = ctrl.Rule(fuzzPositionZ['sedang'] & fuzzPositionX['jauh'], fuzzLongsor['ya'])
    rule17 = ctrl.Rule(fuzzPositionZ['jauh'] & fuzzPositionX['dekat'], fuzzLongsor['tidak'])
    rule18 = ctrl.Rule(fuzzPositionZ['jauh'] & fuzzPositionX['sedang'], fuzzLongsor['ya'])
    rule19 = ctrl.Rule(fuzzPositionZ['jauh'] & fuzzPositionX['jauh'], fuzzLongsor['ya'])

    longsor_control = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6 , rule7,rule8,rule9,rule10, rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19])
    decision = ctrl.ControlSystemSimulation(longsor_control)


    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()
    #client.loop()
