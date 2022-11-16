# distance-tracker

- Can track the distance of the face right now approximately with an error difference of 1-3 cm.
- All the distances are measured in cm.
- 3 parameters/ values are required for this tracking
>- Initial detection distance from the camera
>- Initial height of the detectionbox of face/object
>- Height of the detectionbox of the face/object while moving

- Focal length is found by calculating the inital distance and the initial height of the object 

- Then the distance is found by using the focal length found in the first stage

- Right now this works for only faces because I couldn't find any object images data in openCV..but the concept is the same, just the updation of the xml data is enough.

- This distance is truely based on the accuracy of the detectionbox hence better detection algorithm = better result 
## OUTPUT
<p align="center">
  <img src="https://github.com/0EnIgma1/distance-tracker/blob/main/dist.PNG">
</p>
