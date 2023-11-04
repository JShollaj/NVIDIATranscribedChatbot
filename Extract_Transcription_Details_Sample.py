from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from pytube import YouTube
import os

# List of video IDs
video_ids = ['mKN5u_eZQII', 'AULi-qPW9PM', 'sDFAWnrCqKc', 'xCguHth07MU', 'DR2xtRg3aW8', 'KYNHe_XyUBc', '1wF7RkPi8J8', 'JhHV9PkTOzw', 'rIX4WBZUmWY', 'gTwLLhebOcQ', '2N4tNiiBDWw', 'DDBI0EZgh_g', 'KyDWrnZQu0A', 'tVd4-xL6EBU', 'zRyKI55qEZY', '-oKHGeMj7UE', '4sHSIV-67DM', 'wAInhset83M', 'mNTi1osPSIA', '1RnTSZK9SwM', 'AND3vVVl8YY', 'ynT65hp92SE', '6n95iEFZS_k', 'R8DXpBw8hMg', '0D8O7yBw4h4', 'pUasda84YPE', 'eW2vF8o_7p0', 'omhEoLzsopo', 'XH5t0wEH3d0', 'PQMNCXR-WF8', 'e8sCq0-TY2s', 'azLCUayJJoQ', 'HUkR2PeveqE', 'XdHdgLNLtEE', 'Hg2KibOvnLM', '7woi3bRa4BU', 'n2c_spQuexU', 'ehesid36d4E', 'Buh0BP9RfWc', 'htR19rdBicA', '4KsL2meivhQ', 'lEu-Y_-XitI', 'XfzMQejmCI0', 'iFdVlR6K64I', '65yv4gGmYjQ', '1imqFXWwxaA', 'hy26lNIRdf4', 'uRH2wowjwj0', '7eYFqeyU9P4', '_-xy9xRc6zo', 'LDl0LLcmu24', '0FDhe63q6sM', 'gAcopBnNmGA', '1KvHY3tlhhY', 'nd5LG0Jrb9M', '45tKDdZ04Do', 'vwo7W_jLx8Q', 'otVu5eINmA8', 'hpwZb0XkZSM', 'YHTSdd8-bnc', 'VWdJ4BCtam8', '7xHLDxUaQ7c', 'HXW2dDT0vw4', 'yimNi5dBovo', '57dEPP67XrY', 'TUSQBrGvRjA', 'FrWF1L8jI8c', '74fDoIvxfB4', 'DuhelQAIH68', 'y_qDhW6_i-0', 'ATVOAf_ng9k', 'epe4hNkJUug', 'Gtko-PpIntk', 'TZkIPNVPX6c', 'A8g-cwOwBcE', 'a0soRIiqT1Q', 'BDldPq938rM', '_JgNA82325I', '_JcrLTVmHog', 'L323NxwWW1M', '6LpFd4PzKbI', 'b1ghiZcSqUY', 'HE1oisY3OzQ', 'jZ5TQs7NihU', 'vOrlHMBcat0', 'lg4Q7tHIKaE', '7NRKyXl9j6U', 'H3AQnlpxk0c', 'io4dwSbAUW4', 'eM4nKWy6anA', '0NHnmVTTsjU', 'gxn2tHaps0M', 'tfUur72JhZc', 'amwfHzXaTps', '_5mnVGOxq50', '_aLtQXkxcJ8', 'gwzEIGgSdKI', 'VNiY_TC3k20', 'rIXNXlMFZtg', '-AulvUL7npc', 'JEDAclmYcbM', 'sz42MI4jJmY', '1x_TM1iuDfE', 'JDw5c883F3k', 'JficcrhnO78', 'tJSrmRfTeaY', 'ha0Xqrd_JLc', 'oBL84CeLwKk', 'IeqoQVHbq08', 'JgP2WgNIq_w', 'QqYtqctSK3U', 'UfmPK6A9Kgo', 'K8uruZCBrpg', 'KfcsdhGKb1U', 'BQC-SGdIdD8', 'O50BkP16eZo', 'zD0zDQ-nerQ', 'uYraFCWHjyU', 'Tf4zVroHFzY', 'ca5yc-4V2_Q', 'DasFSM0kS4Q', 'NQDtfSi5QF4', 'fgibRb_8T5I', 'RyEVh1Orv2Y', 'Q753J0qsJ8Q', '2YwTkrmogDg', 'uAs8X5es1DE', 'DZpt_-kky2I', 'UU9Rh00yZMY', 'VzWHK7l7mqg', 'DZBR-xsERsE', 'R7HSMBCQCkY', '5v24oRG_MUE', '8x7oY3xAgek', 'wuSThbzoNlU', '7GgC7tumbQw', 'B48pd_oUFsw', 'D-RHjpSF0GI', 'W1VhDtoTzA4', 'CwDKy0EKwHE', '4nV-GtqggEw', 'Cg1b1_cm-tM', 'epgwD-TMm9U', 'wecvydZo4Wk', '9cSyNtpIqLc', 'pO1NuZhMds8', 'ctow9BO79nA', 'RSs1d3ffu1k', 'eFgsOeHMAW4', 'BihuOz_earw', 'Xk15X9ab7iw', '49rBP1DoOwo', 'ycNk1nj0KsQ', 'WO4KB5VjT2E', 'AGRg6P9y2RA', 'GDVJSGHWtOg', 'DJ2hcC1orc4', 'UDChsxHx1wc', 'cYUNE4i4Q4E', 'FDQVOFG_97Q', '9oRZaWpZKAE', 'afNVwoX_zd0', '1pPTYs-TU8c', '9zmbBQYx8a8', 't5YwqZqLjys', 'B4hcLxa8V5M', '4IpFuKtSDaI', '9DFVc8oIf4g', 'eblxQCLsexM', '8UZGlPheNTQ', 'zotnq7UNOPM', 'HHzNIh72B_Y', 'ess9hN9yznc', '0NfbabJQUSs', 'kSQgfNoTCKY', 'iaFN0F53L6w', 'ymfXmyuTvlA', '79QZrREqD6g', 'F-5s0bMDk5k', '1kOaYiNVgFs', 'w7871kMiAs8', 'JRVZxNngfKY', '5Qdr8AUNYqU', 'CI4zeHmq3S8', 'k6NVxkx0_Mw', 'is7aBZ1_Op0', '93d-0NMOJbY', '7AraPM8dhyc', 'Wy6AMQaPCqs', 'OcWg95Bbhmk', 'PWe8-hZ2x9E', '1GCqUK1_occ', 'vKKCSMfE05A', 'GQhyoru5eE8', 'SonfENaSesw', 'X5SdELeBhFw', 'BLLfIdLe2XQ', '-hwUFUDoeXQ', 'ZZM1zh4hkyI', '6-FhpfwBpXk', 'NzY-ixrRM3k', 'p7pmg2hT8b4', 'iqagh83I63s', 'CJyejVg9LG8', 'qJg-HoF5RHs', 'hveoeW1_mmI', 'uXbpac7jkiE', 'ajegb0W-JbU', 'H1pjWDgPVPw', 'quWGKXAO8m8', 'cACWJyiK47E', 'Rfdtx-Oj54g', 'iOMvi_BR7P0', 'guYIxRnTXfs', 'idSDQ7cqhHU', '9YLJTdNEmEg', 'bxEVMnyXxqw', '8DUmBS3ucIs', 'U57_a3lGKOo', 'SdrW2nIBc9Q', 'mFQY2XySZ0w', 'IWwP4IajMUc', 'WwCe9Woy1jw', 'kx6-IjnuJXk', 'pUgRKDlH7y8', 'S_YmmDS26HQ', 'nIbeyX929xA', 'DE4jawpnJBc', '0e5TRStkkLM', 'SlUouzxBldU', 'rK-jxPPY9V4', 'a9hmgAtDhkg', 'LKR5XIW1lgs', 'VBfci5hYN1c', 'bN4yqHhfAfQ', 'wDWovfGuLqs', '3xxJMtLeFeM', 'zPULoFB1mnQ', 'hJ1xovAZzII', 'hanqTQui498', 'UT09801gmec', 'jnEd3IDsF-I', '0q_mSMvhbFI', 'bHuww-l_Sq0', 'JguZhrin9g4', '8eT7WWkOcow', 'gTiqV3akBIE', 'rj7pRJ9VAO4', 'vh-noM8p8Ss', 'feH4b9_2Oug', 'nY20fDmlW7M', 'AiliuDkVJRs', 'vnpUykzHpv8', 'jGEaBjFMbP0', 'F8xa_CA53jA', 'gN3XeFwZ4ng', '5P0IWJDFjmg', 'sJd670Y2DXI', 'Hki5V0BLDcY', 'UURFgE43PUg', 'yBIKsjd2dJk', 'RwPCgvjRzNo', 'prsrply1GUA', 'RXqnBDAKQSU', '-jT2rqLp5uE', 'ckdHWWpfSpk', 'PXc_SlnT2g0', 'lm5kT4ZlSDM', 'EWK-qIAfkT8', 'JslLeOvXM6s', 'L_JSLZQ2ZFs', 'Hfft98GqRUM', 'gD2y7s-FsX0', 'BM9q8vnjU6w', 'NiXtswuE1MI', '-90jBOnWJhQ', 'pzzT18AawJI', 'UetNXR844Ww', '56tkm95gfFI', 'QWsfohf0Bqk', 'u4mb4F17new', 'sp3kZwKKYfw', 'UbwPmlE9XGg', 'fwI_uSbH4pk', 'H36SkfY7ccs', 'E48LqfvSSOw', 'cu-M8I3YUxM', 'hGnpGi92J84', 'f-CvtA2nuN8', 'ysWz-pJuM1M', 'VxNDH6qLZ_Q', 'kTKk05yzuzo', 'VtkxhygfNsY', '9diFylPvIAQ', 'jiMZYJ--cT8', 'xJtKd2bDS3M', 'WBoUhaBI_B0', 'AQhkMLaB_fY', 'obt60r8ZeB0', 'sN6aT9TpltU', 'QatH8iF0Efk', 'QXIwdsyK7Rw', 'VY7m4lPIOj0', '3Z-BT2p4tiM', 'OC637pfAJs8', 'RhsbjB9iygI', '1rNYgQTQvYc', 'L1QKTPb6V_I', 'PUBHhMyIwlg', 'mwOVFXkc1WI', 'uvU8AXY1170', 'MY_Fe7EN6ro', '9Wv9A6C6U5w', 'LMsUP-W-3FI', 'fueoe2zwero', 'zsjcSapzUfU', 'WcWJBt82HXY', 'fIESu365Sb0', '2T8CG7lDkcU', 'dVGEtWYkP2c', 'JJOmFZKpYTo', 'wBgpMf_KQVw', 'NqmMnjJ6GEg', 'DgZD3FV8Pz4', '48VSHYeGtk4', 'ceBo2dZjZnM', '436x164HMnI', 'xIx1VSVh8NM', 'pudJRaMizb4', 'hsRcahyojtA', 'WDgPZgKOHhs', 'QwksuIu7jQU', 'JIfu7LTzzOg', 'm24GfyFzSX0', 'raGYTyLdXGk', 'itNWdv2Fu-0', '-pg7vyRTj2E', 'AAcw9J5n11k', '6-tU7NxgAts', '7AlnrE8gBaA', 'iqiSJklgT54', 'GAZP1NcdWMo', 'b7QE32Pl6Cg', '9QuDh3W3lOY', 'ZeuM2k_hrq0', 'XPUOWzB1PiY', 'uS4A0tBFLao', 'HiSexy6eoy8', '6O2B9BZiZjQ', 'AODo_RjJoUA', 'Rk5nD8tt_W4', '-oAVJeQxyEY', 'EoQfX1q-VNE', 'ynCxnR1i0QY', '4B2ipB7n5Nk', 'bcM5AQSAzUY', 'r2ewwd4d0vc', 'gBPNO6ruevk', 'QuKBZlRFpiA', '46n1kLsW_6M', 'zPuTfBnqcsw', '_Cg0fHBUzFw', 'F5cAw-u7Bw4', 'w5V7cjbMpJ0', 'rObTbAijx1M', 'r9Q2aXJhmU8', 'y5EJXeEiB1o', 'Ifwf-vq7A6A', 'sI4zHNXdtzk', 'heX5b-Q28KI', 'DWWXaUNVZM4', 'nF_bue13vNc', '3-DTB18tf4I', 'zaOR22Q0RPc', 'PBUb_D2aYJU', 'FqnPGHdh7iM', 'T0Pjki4vXx0', 'MVu8Xde0eCI', 'qiHH5KMHxhA', 'r1V3pB0gN5M', 'e3F3GpXtEfo', '6gAuzAYiVu4', 'Hdew1P1nXBc', 'dG2iNaz1ggc', 'jZzAx6vgPr0', 'H2blB7MGnx4', 'QRs619bWAow', 'kaWtXnlKWQs', 'nY9ogwNdAVc', 'Oz0aeL6dQGs', 'fyhPFTF75tk', 'qzcPBJRJteI', 'jtMoxUyPPXk', '1PidjSrpLAI', 'vwXY5ofOZyk', 'Xu0IogW0FI4', 'A9vrvIEtIWs', 'i1gI_Blvcsg', 'dLK2wuIKjPw', 'Mdr_1Y1MTgw', 'sW-zs6cCHs8', 'pckZFC_hs50', 'vcANdBPmV2c', 'LztHuPh3GyU', '26t8MfP8Fo0', 'Uvu6NNOvhg4', 'GbMfAPIm_W8', 'NWrpHM6N2CE', 'Cn6GA_Nn4BU', 'zgA6wrKzoNQ', 'Dkzp05cpdpw', 'bcJk6HEVFwM', 'xwmUQ0MSdw8', 'WsmyLV4x3Co', 'WjNuHH4GEVo', 'BEjowBF_nko', 'RawWrBq2lE4', 'UpayzsxKr-w', 'WESAD2VYnv4', 'VrQWaegcw7M', 'iYKoDVyOrEE', '_JcpmAkkNac', 'yyR0ZoCeBO8', 'zYVoD2P8ZUA', '-AIzrkEndNI', '-nX8eD7FusQ', '2b0YQddfLfA', 'c0NPovKjEGM', '1CuSRw--mXc', 'sP5SkBwmVOo', 'k9E-YSWQxIU', 'KVDvIi0-nUk', 'Izu_r9XkHus', 'tsWPeZTLpkU', 'qc6tNelLnQ0', '13h_9lX6OZA', 'a10lM0yorMw', 'DgVXny-uTQ0', 'cIHoS_CByZA', 'UPeOUyi_TqA', 'Bb0Xh2Ote04', 'iHM4RyjeV-U', 'UvCHkciaw64', 'iOLVqqHQsBU', 'G3QA3ZzD4oc', 'fiOYDTnO_fU', 'iAavYF-XqTA', 'r3LrCnou1K4', 'uM3Ii79KQ20', 'vMZ7tK-RYYc', 'cL05xtTocmY', 'Tfob-C0o-rc', '4-pwkVyDqCQ', 'QisCRGmidJ4', 'Tyn8pzwpq2k', 'wZsgWKsUt1M', 'l7NPmJP462M', 'kH7B3B4k0SQ', 'QiqTvw1_gyw', 'fYV_DawfuCg', 'rOc6jOrtHZg', 'jeGHCgbg66c', 'mKHbCoEdiKE', 'EmKSxfTBSXM', '-RzfTdEF81w', 'QcNO45EHLW4', 'm4ZpB_Ip2qg', 'AMDiR61f86Y', '7aWVkbAemBg', '9TEJC5fXnu8', 'mCB8WOMmHm4', '0c90TrLS-jo', 'gCCwEf3traM', 'XV37Aj_8Jt0', 'FuwxJL5T3a8', 'RbT4s8nKq28', '7PtqsRJnKVE', 'ZA9Ityyk4pg', 'FOhiltzjbzI', 'nyovHI_WWXc', 'Lzkl2rao0kU', 'DFCpuFEQdak', '370cT-OAzzM', 'H12od3SmtqI', '8UoE2NEh9pE', 'fUPvz0j-1YM', 'sWkjx5Je4Zo', 'l5eparXPc7Q', 'YJswaw-Nlf8', '1zv9fZ3hZS8', '0b93_oVUKn4', 'WE6caN6_Flo', '6OiS3BaLISI', 'vM-41Mv00eU', 'JhuT5i8mXME', 'OcjdZUJiIdM', 'wm4kCy8qNVc', 'Nun1HXqBEVY', 'i9rrVFd5zGM', 'V5Leg6dnw2w', '5Qusn4YLmY0', 'rvMVqPsXL10']

# Directory to save transcripts and metadata
output_directory = 'YouTube_Details'
os.makedirs(output_directory, exist_ok=True)

# Function to get video details
def get_video_details(video_id):
    yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')
    details = {
        'title': yt.title,
        'publish_date': yt.publish_date.strftime('%Y-%m-%d') if yt.publish_date else 'Not available',
        'length': yt.length,
        'views': yt.views,
        'rating': yt.rating,
        'author': yt.author,
        'description': yt.description,
        'thumbnail_url': yt.thumbnail_url,
        'keywords': yt.keywords,
        'channel_id': yt.channel_id,
        'channel_url': yt.channel_url,
        'age_restricted': yt.age_restricted,
        'video_id': yt.video_id
    }
    return details

# Function to download transcript and video details
def download_video_details(video_id):
    try:
        details = get_video_details(video_id)

        # Get transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Prepare path
        output_filename = os.path.join(output_directory, f"{video_id}_details.txt")
        
        # Writing details and transcript to file
        with open(output_filename, 'w', encoding='utf-8') as file:
            for key, value in details.items():
                if key == 'keywords':
                    value = ', '.join(value)
                file.write(f"{key.capitalize()}: {value}\n")
            file.write("\n--- Transcript ---\n\n")
            for entry in transcript:
                file.write(f"{entry['text']}\n")

        print(f"Details and transcript saved for video ID {video_id}")
        
    except TranscriptsDisabled:
        print(f"Transcript is disabled for video ID {video_id}")
    except NoTranscriptFound:
        print(f"No transcript found for video ID {video_id}")
    except Exception as e:
        print(f"An error occurred for video ID {video_id}: {e}")

# Download details
for video_id in video_ids:
    download_video_details(video_id)

print("All video details and transcripts have been processed.")
