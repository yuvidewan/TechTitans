from multicolorcaptcha import CaptchaGenerator
from PIL import UnidentifiedImageError
import os

def generate_and_verify_captcha():
    # 1. Initialize the Captcha Generator
    # The generator will handle creating the image, equation, and answer
    generator = CaptchaGenerator()

    try:
        # 2. Generate a math captcha image
        captcha = generator.gen_math_captcha_image(difficult_level=2)
        
        # 3. Extract the useful information
        image = captcha.image
        equation_str = captcha.equation_str # this is the equation
        correct_answer = captcha.equation_result 

        # 4. Save the generated image so you can see it
        output_directory = "utils"

        # 2. Create the directory if it doesn't already exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # 3. Construct the full path to the image file
        image_filename = os.path.join(output_directory, "captcha_generated.png")
        
        # 4. Save the image to the specified path
        image.save(image_filename)
        
        print(f"CAPTCHA image has been saved as '{image_filename}'")
        print("Please open the image to see the math problem.")
        
        # 5. Prompt the user for the answer
        user_answer = input(f"What is the answer to the problem in the image? :")

        # 6. Verify the answer
        if user_answer.strip() == correct_answer:
            print("\n Correct! You have proven you are human.")
        else:
            print(f"\n Incorrect. The correct answer was: {correct_answer}")

    except UnidentifiedImageError:
        print("Error: Could not generate the CAPTCHA. This can sometimes happen")
        print("if the library's font files are not found. Please try running again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    generate_and_verify_captcha()
