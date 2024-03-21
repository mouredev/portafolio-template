import json


class Media:
    def __init__(self, email, cv, github, likedin):
        self.email = email
        self.cv = cv
        self.github = github
        self.likedin = likedin


class Technology:
    def __init__(self, icon, name):
        self.icon = icon
        self.name = name


class Info:
    def __init__(self, icon, title, subtitle, description, date="", certificate="", technologies=[], image="", url="", github=""):
        self.icon = icon
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.date = date
        self.certificate = certificate
        self.technologies = [Technology(**tech) for tech in technologies]
        self.image = image
        self.url = url
        self.github = github


class Extra:
    def __init__(self, image, title, description, url):
        self.image = image
        self.title = title
        self.description = description
        self.url = url


class Data:
    def __init__(
        self,
            title,
            description,
            image,
            avatar,
            name,
            skill,
            location,
            media,
            about,
            technologies,
            experience,
            projects,
            training,
            extras
    ):
        self.title = title
        self.description = description
        self.image = image
        self.avatar = avatar
        self.name = name
        self.skill = skill
        self.location = location
        self.media = Media(**media)
        self.about = about
        self.technologies = [Technology(**tech) for tech in technologies]
        self.experience = [Info(**info) for info in experience]
        self.projects = [Info(**info) for info in projects]
        self.training = [Info(**info) for info in training]
        self.extras = [Extra(**info) for info in extras]


with open("assets/data/data.json") as file:
    json_data = json.load(file)

data = Data(**json_data)
