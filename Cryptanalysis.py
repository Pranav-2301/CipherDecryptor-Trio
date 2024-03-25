import string
from collections import Counter
import time

all_characters = string.ascii_lowercase + ' '
plaintexts = [
    {"name": "Candidate Plaintext #1",
     "content": "unconquerable tropical pythagoras rebukingly price ephedra barmiest hastes spades fevers cause wisped overdecorates linked smitten trickle scanning cognize oaken casework significate influenceable precontrived clockers defalcation fruitless splintery kids placidness regenerate harebrained liberalism neuronic clavierist attendees matinees prospectively bubbies longitudinal raving relaxants rigged oxygens chronologist briniest tweezes profaning abeyances fixity gulls coquetted budgerigar drooled unassertive shelter subsoiling surmounted frostlike jobbed hobnailed fulfilling jaywalking testabilit"},
    {"name": "Candidate Plaintext #2",
     "content": "protectorates committeemen refractory narcissus bridlers weathercocks occluding orchectomy syncoms denunciation chronaxy imperilment incurred defrosted beamy opticopupillary acculturation scouting curiousest tosh preconscious weekday reich saddler politicize mercerizes saucepan bifold chit reviewable easiness brazed essentially idler dependable predicable locales rededicated cowbird kvetched confusingly airdrops dreggier privileges tempter anaerobes glistened sartorial distrustfulness papillary ughs proctoring duplexed pitas traitorously unlighted cryptographer odysseys metamer either meliorat"},
    {"name": "Candidate Plaintext #3",
     "content": "incomes shoes porcine pursue blabbered irritable ballets grabbed scything oscillogram despots pharynxes recompensive disarraying ghoulish mariachi wickerwork orientation candidnesses nets opalescing friending wining cypher headstrong insubmissive oceanid bowlegs voider recook parochial trop gravidly vomiting hurray friended uncontestable situate fen cyclecars gads macrocosms dhyana overruns impolite europe cynical jennet tumor noddy canted clarion opiner incurring knobbed planeload megohm dejecting campily dedicational invaluable praecoces coalescence dibbuk bustles flay acuities centimeters l"},
    {"name": "Candidate Plaintext #4",
     "content": "rejoicing nectar asker dreadfuls kidnappers interstate incrusting quintessential neglecter brewage phosphatic angle obliquely bean walkup outflowed squib tightwads trenched pipe extents streakier frowning phantasmagories supinates imbibers inactivates tingly deserter steerages beggared pulsator laity salvageable bestrode interning stodgily cracker excisions quanted arranges poultries sleds shortly packages apparat fledge alderwomen halvah verdi ineffectualness entrenches franchising merchantability trisaccharide limekiln sportsmanship lassitudes recidivistic locating iou wardress estrus potboi"},
    {"name": "Candidate Plaintext #5",
     "content": "headmaster attractant subjugator peddlery vigil dogfights pixyish comforts aretes felinities copycat salerooms schmeering institutor hairlocks speeder composers dramatics eyeholes progressives reminiscent hermaphrodism simultaneous spondaics hayfork armory refashioning battering darning tapper pancaked unaffected televiewer mussiness pollbook sieved reclines restamp cohosh excludes homelier coacts refashioned loiterer prospectively encouragers biggest pasters modernity governorships crusted buttoned wallpapered enamors supervisal nervily groaning disembody communion embosoming tattles pancakes"},
    {"name": "Candidate Plaintext #6",
     "content": "durenesses maladdresses earthclosets rentabilities maxwhales secludes unroost weathers taping unseduced trumpety procurers actressed heartens spiders misstepped paleoscene memorializers torturee interdiction reprisers inflects spokesmanship degreases gelcaps epitome widgets feazing catfishes hawkeys emanates blazonries bituminizes tachometrical dogwagged parodists reperused overprint proselyte bronzier javelining extendible congesting laymans gormandizers agnates propaties racketers coeternal routings greeters hindpaws prestress outwalked noneters impends amenities buntlines desert ductilities"},
    {"name": "Candidate Plaintext #7",
     "content": "swashbucklings perpetuation pimping accoutred rebraces subblock slinkily artilleryman commendation glimmered saltish reevaluate unflagellated lissome flutings heartseed newsbrief gradients reoccurring saurels demurrage gatehouses toluidines clastic thalli polarized incalculably abominable ratably chortled nipples sedated newscaster semiclosed rhombuses pluperfects corrodible douching scapegrace unedges furloughs busheled jactitating industerial asseveration interwoven idiolect forelock waddling unentered trichotomize snatchiest localism davenports strobiles economizations cauterized postponing"},
    {"name": "Candidate Plaintext #8",
     "content": "pamphleteer revoiced mastered hornbeams seventen boludes clubbed delogic pamphleteered defiantly swingable plateaux immured perspicuously repassage debouching askaris assister plenitudes supersubtle reprepared lecheries outlash subedits enthusing developable swayback plaything lambency implausibly excelled playworthiness neophilisms umphatic humilities pregrowth domury kroonis fringes lelted bepity religate inducement coenacts rebinding serac refunding quippers palsgrave solidifications catamarans perlitic suspecting unfaithful confabbed parclose rollbacked fashin outrazes unseasoned unfrowned"},
    {"name": "Candidate Plaintext #9",
     "content": "dissuffered revived predooms dubitatively nonpermissive leachmen applicationary overemphatically unfeared sunbathes universals rewhirl coexert consummation philosophizing flamelessly inlarges metaphrase clerkless furiosity tergals chastened unbuoying lectured dulcimers hobbyhorsing childsibondl depicturizes connotated hemizonia emphatic enfolder parcarry divellicate runrounds wash undowried unbeguiling indiscriminating hypersensitate excepts turpidly cadency sinewed warranted worktiming emanatism songfully pohutukawas carvacrols slirtingly coddler selenographic declarants progressmen unconcern"},
    {"name": "Candidate Plaintext #10",
     "content": "financings discrepancies salaamed perseveringly imperatives waterharrier microkarst sashen sweethead poundbase dilaters evelasting immingleable outpoured computation sprouter missalty hemophthises intercessorial landholding nummular abradants diapeded siruped evidently unexhausted venusberg advantages deemphasize unmalleable dispraisingly decretum oestrin tensile monitoring aigrets seminomad gnarling wispy unbearableness unphones tateao distresses dermatoglyphics endorsator remapping mermaid granoses subschemas repliers offpringed thonged tremolantize festinate scolie phlebography superfeeders"}
]

# averaging space frequency from plaintext in this table
letter_frequencies = {
    ' ': 10.00, 'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70,
    'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15,
    'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51,
    'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06,
    'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07
}

'''
plaintext_frequency_1 = {
    ' ': 10.33, 'a': 6.33, 'b': 2.83, 'c': 3.67, 'd': 3.33, 'e': 12.0, 'f': 1.67, 'g': 3.17,
    'h': 1.17, 'i': 8.33, 'j': 0.33, 'k': 1.5, 'l': 5.33, 'm': 0.83, 'n': 6.5, 'o': 4.5,
    'p': 2.0, 'q': 0.33, 'r': 6.33, 's': 7.0, 't': 5.67, 'u': 2.83, 'v': 1.17, 'w': 0.67,
    'x': 0.5, 'y': 1.33, 'z': 0.33
}

plaintext_frequency_2 = {
    ' ': 10.0, 'a': 5.67, 'b': 1.5, 'c': 5.67, 'd': 4.67, 'e': 11.5, 'f': 0.83, 'g': 1.83,
    'h': 1.83, 'i': 7.33, 'j': 0.0, 'k': 0.5, 'l': 4.67, 'm': 2.17, 'n': 4.0, 'o': 5.83,
    'p': 3.33, 'q': 0.0, 'r': 8.33, 's': 6.67, 't': 6.17, 'u': 3.17, 'v': 0.5, 'w': 0.67,
    'x': 0.33, 'y': 2.33, 'z': 0.5
}

plaintext_frequency_3 = {
    ' ': 11.33, 'a': 6.67, 'b': 2.67, 'c': 5.67, 'd': 4.0, 'e': 10.0, 'f': 0.67, 'g': 2.67,
    'h': 2.0, 'i': 8.0, 'j': 0.33, 'k': 0.83, 'l': 4.33, 'm': 2.33, 'n': 7.0, 'o': 6.17,
    'p': 2.5, 'q': 0.0, 'r': 6.33, 's': 6.0, 't': 4.0, 'u': 2.5, 'v': 1.17, 'w': 0.67,
    'x': 0.17, 'y': 2.0, 'z': 0.0
}

plaintext_frequency_4 = {
    ' ': 10.5, 'a': 8.0, 'b': 1.83, 'c': 3.33, 'd': 3.17, 'e': 11.17, 'f': 1.17, 'g': 3.33,
    'h': 2.17, 'i': 8.0, 'j': 0.17, 'k': 1.17, 'l': 4.33, 'm': 1.0, 'n': 6.0, 'o': 3.17,
    'p': 2.83, 'q': 0.67, 'r': 6.83, 's': 8.17, 't': 7.17, 'u': 2.5, 'v': 0.83, 'w': 1.17,
    'x': 0.33, 'y': 1.0, 'z': 0.0
}

plaintext_frequency_5 = {
    ' ': 10.17, 'a': 6.17, 'b': 1.17, 'c': 3.67, 'd': 3.33, 'e': 11.17, 'f': 1.33, 'g': 2.67,
    'h': 2.5, 'i': 6.67, 'j': 0.17, 'k': 0.83, 'l': 3.33, 'm': 3.5, 'n': 5.0, 'o': 6.83,
    'p': 3.5, 'q': 0.0, 'r': 7.5, 's': 8.83, 't': 5.83, 'u': 2.17, 'v': 1.33, 'w': 0.33,
    'x': 0.33, 'y': 1.67, 'z': 0.0
}'''


def calculate_frequencies(text):
    return Counter(text)


def chi_squared(observed, expected):
    chi_sq = 0
    for letter in observed.keys():
        observed_freq = observed.get(letter, 0)
        expected_freq = expected.get(letter, 0)
        chi_sq += ((observed_freq - expected_freq) ** 2) / expected_freq if expected_freq else 0
    return chi_sq


def shift_cipher_decrypt(ciphertext, shift):
    # print(f"Debug - Shift value: {shift}")  # Debug statement to verify shift value
    decrypted_text = ""
    alphabet = " " + string.ascii_lowercase
    for char in ciphertext:
        if char in alphabet:
            char_index = alphabet.index(char)
            shifted_index = (char_index - shift) % len(alphabet)
            decrypted_text += alphabet[shifted_index]
        else:
            decrypted_text += char
    return decrypted_text


def find_plaintext_content(ciphertext, plaintexts):
    for shift in range(27):
        decrypted_text = shift_cipher_decrypt(ciphertext, shift)
        for plaintext in plaintexts:
            if decrypted_text == plaintext["content"]:
                return plaintext["name"], decrypted_text
    return None, None


def find_best_shift_by_chi_squared(ciphertext, letter_frequencies):
    chi_squared_values = []
    for shift in range(27):
        shifted_text = shift_cipher_decrypt(ciphertext, shift)
        observed_frequencies = calculate_frequencies(shifted_text)
        chi_sq = chi_squared(observed_frequencies, letter_frequencies)
        chi_squared_values.append((shift, chi_sq))
    best_shift = min(chi_squared_values, key=lambda x: x[1])[0]
    return shift_cipher_decrypt(ciphertext, best_shift)


def calculate_levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return calculate_levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def find_closest_match_by_levenshtein(guess, plaintexts):
    distances = []
    for plaintext in plaintexts:
        distance = calculate_levenshtein_distance(guess, plaintext["content"])
        distances.append((plaintext["name"], distance))
    closest_match = min(distances, key=lambda x: x[1])
    return closest_match


def find_closest_match_by_partial_content(ciphertext, plaintexts, letter_frequencies):
    best_guess_text = find_best_shift_by_chi_squared(ciphertext, letter_frequencies)
    best_guess_length = len(best_guess_text)
    trimmed_plaintexts = [{"name": pt["name"], "content": pt["content"][:best_guess_length]} for pt in plaintexts]
    closest_match = find_closest_match_by_levenshtein(best_guess_text, trimmed_plaintexts)
    return closest_match


def integrate_all_analyses(ciphertext, plaintexts, letter_frequencies):
    name, decrypted_content = find_plaintext_content(ciphertext, plaintexts)
    if decrypted_content:
        print(f"My plaintext guess is:{decrypted_content}")
    else:
        guessed_plaintext_content = find_best_shift_by_chi_squared(ciphertext, letter_frequencies)
        closest_match = find_closest_match_by_levenshtein(guessed_plaintext_content, plaintexts)
        closest_match_name = closest_match[0]
        closest_content = next((pt['content'] for pt in plaintexts if pt['name'] == closest_match_name), None)
        print(f"My plaintext guess is:{closest_content}")


def integrate_all_analyses_with_length_adjustment(ciphertext, plaintexts, letter_frequencies):
    ciphertext_length = len(ciphertext)  # Determine the length of the input ciphertext
    name, decrypted_content = find_plaintext_content(ciphertext, plaintexts)
    if decrypted_content:
        # If a full match is found, trim the output to match the input length
        print(f"My plaintext guess is:{decrypted_content[:ciphertext_length]}")
    else:
        # Find the best guess based on chi-squared analysis
        best_guess_text = find_best_shift_by_chi_squared(ciphertext, letter_frequencies)
        # Adjust the best guess to the input length for comparison
        best_guess_text = best_guess_text[:ciphertext_length]
        # Find the closest match by trimming plaintexts to the best guess length before comparing
        trimmed_plaintexts = [{"name": pt["name"], "content": pt["content"][:ciphertext_length]} for pt in plaintexts]
        closest_match = find_closest_match_by_levenshtein(best_guess_text, trimmed_plaintexts)
        closest_match_name = closest_match[0]
        # Retrieve the closest matching content, adjusted to the input length
        closest_content = next(
            (pt['content'][:ciphertext_length] for pt in plaintexts if pt['name'] == closest_match_name), None)
        print(f"My plaintext guess is:{closest_content}")


if __name__ == "__main__":
    ciphertext = input("Enter the ciphertext:")
    integrate_all_analyses_with_length_adjustment(ciphertext, plaintexts, letter_frequencies)
