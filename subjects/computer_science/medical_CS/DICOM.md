###### DICOM
    digital imaging and communications in medicine (DICOM)
- used for storing and trasmitting medical images. adopted @hospitals.
- DICOM defines protocols for image exchange
- developed @ACR and NEMA. was once v difficult to decode images that the machines generated apart from the actual manufacturers.
- DICOM implemented on all medical imaging machines and software whicht view the images (PACS)
- an issue of DICOM is optional fields - can allow incontistency in saving data (egfields are left blnank etc.)
- DICOM images can contain executable code (could store malware)

# Data format
- groups information into datasets, labelled by tags: ID, name etc. then the pixel data. the attrivute may contain multiple frames. 
- pixel data can be compressed eg @JPEG.
- to display hte pixel data, the DICOM committee developed the IDCOM GSDF (display function) - a lookup curve
- file of CXR may contain patient ID within the file

# Services
- mostly network services (transmission)



# pydicom
- allows reading DICOM files, parse into python objects locally for manipulation. can then write/ overwrite DICOM files.
- not about viewing images, rather manipulate data elements in DICOM files.

# DCMTK
- supported @windows and unix OS
- storescp
    + listens on a specific TCP/ IP port for incoming associations from a sotrage service class 8usuer and can receive DICOMS. by default listens on poort 104
