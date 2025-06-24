import os
from pickle import load
import facebook
import extractdata
import generatecaption
from keras.models import load_model


if __name__ == '__main__':
        token = 'EAAF8K7TUhd4BAPZCBAKoijkNbJfSDkRIJxsrij1GG0ZB2yBuHp3e1uZC7wAL2d2qeUDTVvi0viejHhlNSM7ppZCRVbN7n44dh5e4ZAG7UbX6aaEnOVvOFRig5k9YdZBZA12pr9Kwgt8WlITHBZAewe8EvM3s3P4UwxeSReo3QnHWT382Vg8sSoP3aasPFKSuZCSXoXsymvRFKlXXOYkDb2FKy9WmNW1USGcwhZCfqha91ewwZDZD'
        graph = facebook.GraphAPI(token)
        full_name = extractdata.retrieveName(graph)
        all_posts = extractdata.retrievePosts(graph)
        sorted_data = extractdata.sortByTimeStamp(all_posts)
        extractdata.saveImages(sorted_data)

        # Image captioning
        # load the tokenizer
        tokenizer = load(open('tokenizer.pkl', 'rb'))
        # pre-define the max sequence length (from training)
        max_length = 34
        # load the model
        model = load_model('model-ep004-loss3.546-val_loss3.889.h5')
        # load and prepare the photograph
        vggmodel = generatecaption.create_model()
        captions = []
        counter = 0
        for filename in os.listdir('Images'):
            photo = generatecaption.extract_features("Images/" + filename, vggmodel)
            description = generatecaption.generate_desc(model, tokenizer, photo, max_length)
            description = description.split(' ', 1)[1]
            description = description.rsplit(' ', 1)[0]
            captions.append(description)
            counter += 1

        script = "Script start: "
        captionInd = 0

        for post in sorted_data:
            script += extractdata.dateToString(post[0])
            script += " you posted "
            script += post[1]
            if post[2] != "":
                script += " with a photo of " + captions[captionInd]
                captionInd += 1
            script += ". "

        print (script)
