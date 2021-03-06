# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-30 11:24
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('street', models.CharField(blank=True, max_length=30, null=True)),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(max_length=50, null=True)),
                ('text', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BloodExtraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'new'), (1, 'ready for expedition'), (2, 'shipped')], default=0)),
                ('barcode', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('postpone', models.DateField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BloodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'AB'), (3, '0')])),
                ('RH', models.BooleanField(choices=[(True, '+'), (False, '-')])),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('active_acount', models.BooleanField(default=False)),
                ('email_verification_token', models.CharField(max_length=100, null=True)),
                ('personal_identification_number', models.DecimalField(decimal_places=0, max_digits=20)),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'female'), (0, 'male')], default=0)),
            ],
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='NTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location_info', models.CharField(max_length=50, null=True)),
                ('gps_lon', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('gps_lat', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('other_contact', models.CharField(max_length=255)),
                ('info', models.CharField(max_length=255)),
                ('id_boss', models.IntegerField()),
                ('secret_key', models.CharField(max_length=255, null=True)),
                ('id_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='isnts.Address')),
            ],
        ),
        migrations.CreateModel(
            name='OfficeHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.SmallIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('open_time', models.TimeField(blank=True)),
                ('close_time', models.TimeField(blank=True)),
                ('id_nts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isnts.NTS')),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=3, max_digits=6)),
                ('height', models.DecimalField(decimal_places=6, max_digits=6)),
                ('phone', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created', to='isnts.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.PositiveSmallIntegerField(choices=[(1, 'Have you ever donated blood, plasma or blood cells in the past?'), (2, 'Have you ever been excluded from blood donation as ineligible?'), (3, 'Are you in good health?'), (4, 'Is your weight over 50 kg?'), (5, 'Have you been treated by a dentist or dental hygienist in the past 72 hours ?'), (6, 'Have you been using any medication in the past month? Which medication?'), (7, 'Have you suffered from fever over 38°C, herpes, diarrhea, sucked in tick, animal bite in the past month?'), (8, 'Have you been vaccinated in the past month?'), (9, 'Have you ever suffered or are you currently suffering from infectious disease such as: tuberculosis, boreliosis, toxoplasmosis, brucellosis, infectious mononucleosis, listeriosis, tularemia, babesiosis, Q-fever?'), (10, 'Have you ever suffered or are you currently suffering from tropical disease: malaria, leishmaniasis, Chagas disease (trypanosomiasis)?'), (11, 'Have you ever suffered or are you currently suffering from rheumatic disorders, rheumatic fever or autoimmune disease?'), (12, 'Have you ever suffered or are you currently suffering from heart disease, high or low blood pressure?'), (13, 'Have you ever suffered or are you currently suffering from chronic lung or bronchi disease, asthma, allergy, hay fever/pollinosis?'), (14, 'Have you ever suffered or are you currently suffering from kidney disease?'), (15, 'Have you ever suffered or are you currently suffering from blood disease, bleeding/hemorrhage symptoms?'), (16, 'Have you ever suffered or are you currently suffering from nervous system disease, epilepsy?'), (17, 'Have you ever suffered or are you currently suffering from metabolism disorders (for ex. diabetes) or endocrine disease (for ex. thyroid gland disease)?'), (18, 'Have you ever suffered or are you currently suffering from skin diseases (eczema, psoriasis)?'), (19, 'Have you ever suffered or are you currently suffering from digestive system, liver or pancreas disease?'), (20, 'Have you ever suffered or are you currently suffering from tumor disease?'), (21, 'Have you ever suffered or are you currently suffering from tumor disease?'), (22, 'Have you ever suffered or are you currently suffering from sexually transmissible disease?'), (23, 'Have you experienced an inexplicable weight loss, raised temperature, sweating, behavioral changes, enlarged lymphatic nods in the past twelve months?'), (24, 'Have you been treated for acne by isotretinoine (RoaccutaneR, AccutaneR), for prostate by finasteride or dutasterid (ProscarR, AvodartR, DuodartR), and for baldness (PropeciaR) in the past three months?'), (25, 'Have you been treated by acitretin (NeotigasonR) or etretinate (TegisonR ) in the past three years?'), (26, 'In the past six months have you had any operation, medical examination or treatment, endoscopy , arterial catheterization?'), (27, 'In the past six months have you had any tattooing, piercing, ear-ring application, acupuncture, permanent make – up ?'), (28, 'In the past six months have you had any injury during which the wound or mucous membrane was in contact with another person’s blood, or any accidental stick of a used needle?'), (29, 'Have you ever received a blood component transfusion? If yes, when?.where?'), (30, 'Have you ever received human or animal tissue or organ transplant (e.g. corneal transplantation, dura mater graft….)?'), (31, 'Have you ever undergone brain or spinal cord surgery ?'), (32, 'Have you had any information about Creutzfeldt-Jacob disease or about another spongiform encephalopathy in your family?'), (33, 'Have you ever been treated with a products prepared from hypophysis (e.g. growth hormone)?'), (34, 'Did you spend the time in excess of six moths in the United Kingdom/Ireland during 1980–1996?'), (35, 'Have you been out of Slovak Republic in the past six months?'), (36, 'Were you born or have you ever lived more than 6 month out of Europe? If yes, where? Since when do you live in Europe?'), (37, 'Have you been in contact with any person suffering from hepatitis or another infectious disease in the past six months, ?'), (38, 'Have you had a sexual intercourse with new partner in the past three months?'), (39, 'Have you or your sexual partner ever been in any of the following risk situations: positive test for the HIV or hepatitis (jaundice)?'), (40, 'Have you or your sexual partner ever been in any of the following risk situations: use of drugs or anabolic hormones?'), (41, 'Have you or your sexual partner ever been in any of the following risk situations: payment for sex or performing sex for money or drugs?'), (42, 'Do you have a risky occupation/hobbies? (professional driver, diver, worker in the height)?'), (43, 'Male Donors: Have you had a sexual intercourse with a man in the past twelve months?'), (44, 'Female Donors: Have you been pregnant or breast feeding in the past six months?'), (45, 'Female Donors: Have you been treated with hormonal injection for sterility before 1986 ?')])),
                ('answer', models.PositiveSmallIntegerField(choices=[(0, 'no'), (1, 'yes'), (2, 'not sure')])),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isnts.Questionnaire')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.PositiveSmallIntegerField(choices=[(0, 'Bratislavsky'), (1, 'Nitriansky'), (2, 'Trnavsky'), (4, 'BanskoBystricky'), (5, 'Zilinsky'), (6, 'Kosicky'), (7, 'Presovsky'), (3, 'Trenciansky')])),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('id_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='isnts.Region')),
            ],
        ),
        migrations.CreateModel(
            name='DonorCard',
            fields=[
                ('donor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='isnts.Donor')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_num', models.CharField(blank=True, max_length=20)),
                ('card_created_date', models.DateTimeField(auto_now_add=True)),
                ('info', models.CharField(blank=True, max_length=255, null=True)),
                ('can_donate_from', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('isnts.donor',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='id_donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isnts.Donor'),
        ),
        migrations.AddField(
            model_name='employee',
            name='id_nts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='isnts.NTS'),
        ),
        migrations.AlterUniqueTogether(
            name='donor',
            unique_together=set([('personal_identification_number',)]),
        ),
        migrations.AddField(
            model_name='booking',
            name='id_answer_sheet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='isnts.Questionnaire'),
        ),
        migrations.AddField(
            model_name='booking',
            name='id_donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isnts.Donor'),
        ),
        migrations.AddField(
            model_name='booking',
            name='id_employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='isnts.Employee'),
        ),
        migrations.AddField(
            model_name='booking',
            name='id_nts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isnts.NTS'),
        ),
        migrations.AddField(
            model_name='bloodextraction',
            name='blood_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isnts.BloodType'),
        ),
        migrations.AddField(
            model_name='bloodextraction',
            name='id_donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isnts.Donor'),
        ),
        migrations.AddField(
            model_name='bloodextraction',
            name='id_nts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='isnts.NTS'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='id_nts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isnts.NTS'),
        ),
        migrations.AddField(
            model_name='address',
            name='town',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='isnts.Town'),
        ),
        migrations.AlterUniqueTogether(
            name='questions',
            unique_together=set([('questionnaire', 'question')]),
        ),
        migrations.AddField(
            model_name='donorcard',
            name='card_created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='isnts.Employee'),
        ),
        migrations.AddField(
            model_name='donorcard',
            name='id_address_perm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='perm', to='isnts.Address'),
        ),
        migrations.AddField(
            model_name='donorcard',
            name='id_address_temp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='temp', to='isnts.Address'),
        ),
        migrations.AddField(
            model_name='donorcard',
            name='id_blood_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='isnts.BloodType'),
        ),
    ]
