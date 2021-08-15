class Radio:
    __color = 'Brown'
    __brand = "Philips"
    __ACPower = False
    __headphone = False    
    
    def __init__(self):
      
        self._power_led = "ON"
        self._mode_led = None
        self._frequency = 0.0
        self._volume = 0
        print("Your Radio is Ready to be Played ")

    def power_switch(self,power_status):
        self._power_led = power_status
        print("Your Radio Power is " + str(self._power_led))

    def mode_switch(self,mode_status):
        self._mode_led = mode_status
        print("Your Radio Mode is set to " + str(self._mode_led))
    
    def band_tuner(self,freq_value):
        self._frequency = freq_value
        print("Your Radio frequency is set to " + str(self._frequency))

    def volume_tuner(self,vol_value):
        self._volume = vol_value
        print("Your Radio volume is set to " + str(self._volume))

    def __str__(self):
        print("Color of my Radio = " + str(Radio.__color))
        print("Brand of my Radio = " + str(Radio.__brand))

my_radio = Radio()
my_radio.power_switch("ON")
my_radio.mode_switch("AM")
my_radio.band_tuner(101.8)
my_radio.volume_tuner(3)
my_radio.power_switch("ON")
my_radio.__str__()

my_radio = None


