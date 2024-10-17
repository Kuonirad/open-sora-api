from open_sora import OpenSoraAPI

def main():
    api = OpenSoraAPI()
    prompt = "A beautiful sunset over the ocean"
    try:
        result = api.generate_video(prompt)
        print(f"Video generation result for prompt '{prompt}':")
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
