import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    print("say now")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
    # Just pass a language parameter
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    # try:
    #     response["transcription"] = recognizer.recognize_sphinx(audio)
    # except sr.RequestError:
    #     # API was unreachable or unresponsive
    #     response["success"] = False
    #     response["error"] = "API unavailable"
    # except sr.UnknownValueError:
    #     # speech was unintelligible
    #     response["error"] = "Unable to recognize speech"

    return response
if __name__ == "__main__":
    # set the list of words, maxnumber of guesses, and prompt limit
    PROMPT_LIMIT = 5
    ifStill = True
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()


    r = sr.Recognizer()
    mic = sr.Microphone()
    # print(recognize_speech_from_mic(r,mic))
    # get the guess from the user
    # if a transcription is returned, break out of the loop and
    #     continue
    # if no transcription returned and API request failed, break
    #     loop and continue
    # if API request succeeded but no transcription was returned,
    #     re-prompt the user to say their guess again. Do this up
    #     to PROMPT_LIMIT times
    while ifStill:

        for j in range(PROMPT_LIMIT):
            print("say something")
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            # print("I didn't catch that. What did you say?\n")
            print(guess)
        getInput = input("you want more ? y for yes")
        if getInput != 'y':
            ifStill = False


