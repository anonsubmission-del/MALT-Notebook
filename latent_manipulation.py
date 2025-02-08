# In[0] # Load Utility Functions:
from load_generative_model import latent_model, load_audio
from IPython.display import Audio, display
from gui import interface
import librosa as li

# Working with trajectories in latent audio models

# In[1] # Pick Model:
model_name: str = 'percussion'
model_location:str = 'generative_models/'+model_name+'.ts'
model = latent_model([model_location])
sr: int =44100

# In[2] # Pick Audio Sample:
audio_location: str = 'audio/45536__jesuswaffle__hihat3.wav' # HiHat3.wav by jesuswaffle -- https://freesound.org/s/45536/ -- License: Creative Commons 0
audio, sr = li.load(audio_location,sr=44100)
Audio(audio, rate=sr)

# In[3] # Mess with Latent Space:
user_interface = interface(model,audio)   
display(user_interface.app)
# %%
