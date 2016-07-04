#
# lepton pT scales
# Run II numbers for electrons from here https://indico.cern.ch/event/402608/contribution/1/attachments/1206871/1758949/DPG_reReco_corrections.pdf 
# numbers in % 
#leppTresolution = {}

leppTresolution['ele'] = [
    #   pt           eta          smear 
    ( (0.0, 10.0),  (0.0, 1.0),    (0.0003)  ),
    ( (0.0, 10.0),  (1.0, 1.4442), (0.0012) ),
    ( (0.0, 10.0),  (1.566, 2.0),  (0.0011) ),
    ( (0.0, 10.0),  (2.0, 2.5),    (0.0005)  ),
    ( (10.0, 20.0), (0.0, 1.0),    (0.0003)  ),
    ( (10.0, 20.0), (1.0, 1.4442), (0.0012) ),
    ( (10.0, 20.0), (1.566, 2.0),  (0.0011) ),
    ( (10.0, 20.0), (2.0, 2.5),    (0.0005)  ),
    ( (20.0, 30.0), (0.0, 1.0),    (0.0003)  ),
    ( (20.0, 30.0), (1.0, 1.4442), (0.0012) ),
    ( (20.0, 30.0), (1.566, 2.0),  (0.0011) ),
    ( (20.0, 30.0), (2.0, 2.5),    (0.0005)  ),
    ( (30.0, 40.0), (0.0, 1.0),    (0.0003)  ),
    ( (30.0, 40.0), (1.0, 1.4442), (0.0012) ),
    ( (30.0, 40.0), (1.566, 2.0),  (0.0011) ),
    ( (30.0, 40.0), (2.0, 2.5),    (0.0005)  ),
    ( (40.0, 50.0), (0.0, 1.0),    (0.0003)  ),
    ( (40.0, 50.0), (1.0, 1.4442), (0.0012) ),
    ( (40.0, 50.0), (1.566, 2.0),  (0.0011) ),
    ( (40.0, 50.0), (2.0, 2.5),    (0.0005)  ),
    ( (50.0, 200.0),(0.0, 1.0),    (0.0003)  ),
    ( (50.0, 200.0),(1.0, 1.4442), (0.0012) ),
    ( (50.0, 200.0),(1.566, 2.0),  (0.0011) ),
    ( (50.0, 200.0),(2.0, 2.5),    (0.0005)  ),

                     ] 