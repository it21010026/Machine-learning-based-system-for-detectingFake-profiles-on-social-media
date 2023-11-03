from Faker import Faker
import csv

fake = Faker()

# Generate 500 fake profiles
fake_profiles = []
for _ in range(50000):
    profile = {
        'username': fake.user_name(),
        'email': fake.email(),
        'age': fake.random_int(min=18, max=25),
        'gender': 'female',
        'location': fake.city(),
        'occupation': 'student',
        'followers': fake.random_int(min=0, max=1000),
        'posts': fake.random_int(min=0, max=100),
        'is_fake': 1,
    }
    fake_profiles.append(profile)

# Generate 500 real profiles
real_profiles = []
for _ in range(50000):
    profile = {
        'username': fake.user_name(),
        'email': fake.email(),
        'age': fake.random_int(min=26, max=65),
        'gender': fake.random_element(elements=('male', 'female')),
        'location': fake.city(),
        'occupation': fake.job(),
        'followers': fake.random_int(min=0, max=10000),
        'posts': fake.random_int(min=0, max=500),
        'is_fake': 0,
    }
    real_profiles.append(profile)

# Combine the fake and real profiles
profiles = fake_profiles + real_profiles

# Write the profiles to a CSV file
with open('social_media_profiles2.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=profiles[0].keys())
    writer.writeheader()
    for profile in profiles:
        writer.writerow(profile)

