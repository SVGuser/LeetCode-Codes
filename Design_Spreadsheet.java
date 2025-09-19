import java.util.*;

class Spreadsheet {
    private Map<String, Integer> cells;

    public Spreadsheet(int rows) {
        // No need to store rows explicitly since cell references are validated externally
        cells = new HashMap<>();
    }

    public void setCell(String cell, int value) {
        cells.put(cell, value);
    }

    public void resetCell(String cell) {
        cells.remove(cell); // Unset the cell so it defaults to 0
    }

    public int getValue(String formula) {
        formula = formula.substring(1); // Remove '='
        String[] parts = formula.split("\\+");
        int sum = 0;

        for (String part : parts) {
            if (Character.isDigit(part.charAt(0))) {
                sum += Integer.parseInt(part);
            } else {
                sum += cells.getOrDefault(part, 0);
            }
        }

        return sum;
    }
}
