class uid_generator {
    public static String generateUID() {
        int total_chars = 18;
        String chars = "abcdefghijklmnopqrstuvwxyz1234567890";
        StringBuilder uid = new StringBuilder();
        for (int i = 0; i <= total_chars; i++) {
            uid.append(chars.charAt((int) Math.floor(Math.random() * (chars.length() - 1))));
        }
        return uid.toString();
    }

    public static void main(String[] args) {
        System.out.println(generateUID());
    }
}