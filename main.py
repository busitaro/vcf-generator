import pandas as pd

input_file = './numbers.csv'
output_file = './output.vcf'


def read_csv():
    return pd.read_csv(input_file, encoding='utf-8')


def make_vcf_str(data: pd.Series) -> str:
    vcf_str = """BEGIN:VCARD
VERSION:3.0
PRODID:-//Apple Inc.//iOS 14.6//EN
N:{family_name};{first_name};;;
FN:{name}
X-PHONETIC-FIRST-NAME:{first_name_kana}
X-PHONETIC-LAST-NAME:{family_name_kana}
TEL;type=CELL;type=VOICE;type=pref:{tel}
REV:2022-06-08T00:05:59Z
END:VCARD
""".format(
        family_name=data['family_name'],
        first_name=data['first_name'],
        name=data['name'],
        first_name_kana=data['first_name_kana'],
        family_name_kana=data['family_name_kana'],
        tel=data['tel']
    )
    return vcf_str


def output_to_file(data: pd.Series):
    output_str = ''.join(data)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_str)


def main():
    df = read_csv()
    vcf_strs = df.apply(make_vcf_str, axis=1)
    output_to_file(vcf_strs)


if __name__ == '__main__':
    main()
